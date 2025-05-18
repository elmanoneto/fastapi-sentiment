import fastapi.testclient
import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.api.v1.endpoints.sentiment import get_db
from app.db.db import Base
from app.main import app

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield fastapi.testclient.TestClient(app)
    Base.metadata.drop_all(bind=engine)


def test_analyze_create_and_return(client):
    payload = {"text": "Esse projeto é muito bom!"}
    response = client.post("/api/v1/sentiment/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == payload["text"]
    assert data["sentiment"] in ["positive", "neutral", "negative"]
    assert isinstance(data["score_positive"], float)
    assert isinstance(data["score_negative"], float)


def test_list_messages(client):
    response = client.get("/api/v1/sentiment/messages")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert "content" in data[0]
    assert "sentiment" in data[0]
    assert "score_negative" in data[0]
    assert "score_positive" in data[0]
