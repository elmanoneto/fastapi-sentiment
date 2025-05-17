import os

from db.migrate import apply_migrations
from fastapi import FastAPI

from app.api.v1.routes import router as api_router

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")


if os.getenv("ENV") == "production":
    apply_migrations()


@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
