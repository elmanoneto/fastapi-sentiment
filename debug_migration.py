import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

url = os.getenv("DATABASE_URL")
print("Conectando ao banco:", url)

engine = create_engine(url)
with engine.connect() as conn:
    result = conn.execute(text("PRAGMA table_info(messages);"))
    print("Colunas da tabela messages:")
    for row in result:
        print(row)
