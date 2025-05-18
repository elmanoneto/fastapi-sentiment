import os

from dotenv import load_dotenv

from alembic import command
from alembic.config import Config
from app.db.db import DATABASE_URL


def apply_migrations():
    print("🔁 Verificando migrations via Alembic (modo Python)")

    # Caminho absoluto da raiz do projeto
    current_dir = os.path.dirname(__file__)  # app/db
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    alembic_ini_path = os.path.join(project_root, "alembic.ini")
    migrations_path = os.path.join(
        project_root, "alembic"
    )  # <- aqui está o script_location
    dotenv_path = os.path.join(project_root, ".env")

    if not os.path.exists(alembic_ini_path):
        raise FileNotFoundError(f"❌ alembic.ini não encontrado em: {alembic_ini_path}")
    if not os.path.exists(migrations_path):
        raise FileNotFoundError(
            f"❌ Pasta de migrations não encontrada em: {migrations_path}"
        )

    load_dotenv(dotenv_path)

    alembic_cfg = Config(alembic_ini_path)
    alembic_cfg.set_main_option("script_location", migrations_path)
    alembic_cfg.set_main_option("sqlalchemy.url", DATABASE_URL)

    print("📦 Banco de dados:", alembic_cfg.get_main_option("sqlalchemy.url"))
    print("📁 Script location:", alembic_cfg.get_main_option("script_location"))

    command.upgrade(alembic_cfg, "head")
    print("✅ Migrations aplicadas com sucesso.")
