import os
import sys

from app.db import Base, engine

# Adiciona o diretório raiz ao sys.path para encontrar o pacote 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("🛠 Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created.")
