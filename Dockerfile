FROM python:3.12-slim

WORKDIR /app

# Instala dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install poetry

# Copia arquivos de dependência
COPY pyproject.toml poetry.lock README.md ./

# Instala só as dependências, sem tentar empacotar o projeto
RUN poetry install --no-root

# Copia o restante do código
COPY . .

# Expõe a porta da aplicação
EXPOSE 8000

# Roda a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
