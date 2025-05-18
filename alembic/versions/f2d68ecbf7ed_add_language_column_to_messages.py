"""add language column to messages

Revision ID: f2d68ecbf7ed
Revises: a621e7bc45f1
Create Date: 2025-05-18 12:29:13.265833

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f2d68ecbf7ed"
down_revision: Union[str, None] = "a621e7bc45f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "messages",
        sa.Column("language", sa.String(), nullable=False, server_default="pt"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("messages", "language")
