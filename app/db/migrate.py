from alembic import command
from alembic.config import Config


def apply_migrations():
    print("🔁 Verificando migrations via Alembic (modo Python)")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("✅ Migrations aplicadas (ou nenhuma pendente).")
