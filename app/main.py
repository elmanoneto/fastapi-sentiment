from fastapi import FastAPI

from app.api.v1.routes import router as api_router
from app.db.migrate import apply_migrations

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")


apply_migrations()


@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
