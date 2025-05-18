from deep_translator import GoogleTranslator
from fastapi import APIRouter, Depends
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from pydantic import BaseModel, ConfigDict
from pytest import Session

from app.db.db import SessionLocal
from app.models.models import Message
from app.services.sentiment import analyze_sentiment_service


class SentimentalRequest(BaseModel):
    text: str


class SentimentalResponse(BaseModel):
    sentiment: str
    score_positive: float
    score_negative: float
    content: str
    language: str

    model_config = ConfigDict(from_attributes=True)


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/analyze", response_model=SentimentalResponse)
def analyze_sentiment(request: SentimentalRequest, db: Session = Depends(get_db)):
    try:
        detected_language = detect(request.text)
    except LangDetectException:
        detected_language = "unknown"

    translated = GoogleTranslator(source="auto", target="en").translate(request.text)
    sentiment, score = analyze_sentiment_service(translated)
    content = request.text

    message = Message(
        content=content,
        sentiment=sentiment,
        score_positive=score,
        score_negative=1 - score,
        language=detected_language,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


@router.get("/messages", response_model=list[SentimentalResponse])
def get_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Message).offset(skip).limit(limit).all()
