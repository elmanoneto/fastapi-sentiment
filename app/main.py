from contextlib import asynccontextmanager

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from app.api.v1.routes import router as api_router
from app.db.db import SessionLocal
from app.services.cleanup import delete_old_messages

scheduler = BackgroundScheduler()


def cleanup_job():
    db = SessionLocal()
    try:
        delete_old_messages(db)
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not scheduler.running:
        scheduler.add_job(cleanup_job, "interval", days=1)
        scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(title="Sentiment Analysis API", version="1.0.0", lifespan=lifespan)


@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")
