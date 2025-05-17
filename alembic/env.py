import os
import sys
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context
from app.db.db import Base
from app.models.models import Message  # noqa: F401

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv()

# Alembic Config
config = context.config
fileConfig(config.config_file_name)

# Define a URL do banco a partir do .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Define a metadata para autogeração de migrations
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Rodar as migrações em modo offline (gera SQL em texto)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Rodar as migrações em modo online (executa no banco)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
