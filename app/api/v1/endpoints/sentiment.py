from deep_translator import GoogleTranslator
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.sentiment import analyze_sentiment_service


class SentimentalRequest(BaseModel):
    text: str


class SentimentalResponse(BaseModel):
    sentiment: str
    score: float


router = APIRouter()


@router.post("/analyze", response_model=SentimentalResponse)
def analyze_sentiment(request: SentimentalRequest):
    translated = GoogleTranslator(source="auto", target="en").translate(request.text)
    sentiment, score = analyze_sentiment_service(translated)

    return SentimentalResponse(sentiment=sentiment, score=score)
