from fastapi import APIRouter

from app.api.v1.endpoints import sentiment

router = APIRouter()
router.include_router(
    sentiment.router, prefix="/sentiment", tags=["Sentiment Analysis"]
)
