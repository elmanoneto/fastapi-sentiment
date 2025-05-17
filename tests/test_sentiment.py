from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_positive():
    response = client.post(
        "/api/v1/sentiment/analyze", json={"text": "O produto é muito bom!"}
    )
    assert response.status_code == 200
    result = response.json()
    assert result["sentiment"] == "positive"
    assert result["score"] > 0.5


def test_analyze_negative():
    response = client.post(
        "/api/v1/sentiment/analyze", json={"text": "O produto é muito ruim!"}
    )
    assert response.status_code == 200
    result = response.json()
    assert result["sentiment"] == "negative"
    assert result["score"] <= -0.2
