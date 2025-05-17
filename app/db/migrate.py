import logging
import subprocess


def apply_migrations():
    logging.info("🔁 Verify and apply migrations with Alembic...")
    try:
        result = subprocess.run(
            ["alembic", "upgrade", "head"], capture_output=True, text=True, check=True
        )
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("❌ Error applying migrations:")
        logging.error(e.stderr)
