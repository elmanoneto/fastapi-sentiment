import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.routes import router as api_router
from app.db.migrate import apply_migrations


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("RUN_MIGRATIONS", "false").lower() == "true":
        apply_migrations()
    yield


app = FastAPI(title="Sentiment Analysis API", version="1.0.0", lifespan=lifespan)


@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
