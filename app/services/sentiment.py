from deep_translator import GoogleTranslator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment_service(text: str) -> tuple[str, float]:
    translated = GoogleTranslator(source="auto", target="en").translate(text)
    result = analyzer.polarity_scores(translated)
    score = result["compound"]

    if score > 0.1:
        sentiment = "positive"
    elif score < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, score
