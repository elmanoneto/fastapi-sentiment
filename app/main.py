from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

load_dotenv()

app = FastAPI()

analyzer = SentimentIntensityAnalyzer()

class SentimentalRequest(BaseModel):
    text: str
    
class SentimentalResponse(BaseModel):
    sentiment: str
    score: float

@app.get("/health")
def health_check():
    return { "status": "ok" }

@app.post("/sentiment", response_model=SentimentalResponse)
def analyze_sentiment(request: SentimentalRequest):
    translated = GoogleTranslator(source='auto', target='en').translate(request.text)
    result = analyzer.polarity_scores(translated)
    score = result["compound"]
    
    if score > 0.1:
        sentiment = "positive"
    elif score < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return SentimentalResponse(sentiment=sentiment, score=score)