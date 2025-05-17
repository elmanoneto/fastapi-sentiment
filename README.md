# fastapi-sentiment-api

API para análise de sentimentos com FastAPI + VADER + tradução automática com deep-translator.  
Inclui endpoint `/sentiment` que retorna `positive`, `neutral` ou `negative`.

## Rodar localmente

```bash
poetry install
poetry run uvicorn app.main:app --reload
