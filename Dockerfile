FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential curl

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Cria diretório da aplicação
WORKDIR /app

# Copia arquivos
COPY pyproject.toml poetry.lock README.md ./
RUN poetry install

COPY . .

# Define comando padrão
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
