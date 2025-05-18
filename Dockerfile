FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock README.md ./
RUN poetry install --no-root

COPY . .
COPY alembic.ini alembic.ini
COPY alembic alembic

EXPOSE 8000

CMD poetry run alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000