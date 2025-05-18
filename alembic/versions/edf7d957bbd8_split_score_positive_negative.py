"""split score positive negative

Revision ID: edf7d957bbd8
Revises: f2d68ecbf7ed
Create Date: 2025-05-18 13:58:37.089865

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "edf7d957bbd8"
down_revision: Union[str, None] = "f2d68ecbf7ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("messages", sa.Column("score_positive", sa.Float(), nullable=True))
    op.add_column("messages", sa.Column("score_negative", sa.Float(), nullable=True))

    op.execute(
        """
        UPDATE messages
        SET score_positive = score,
            score_negative = 1 - score
    """
    )

    op.drop_column("messages", "score")

    if op.get_bind().dialect.name != "sqlite":
        op.alter_column("messages", "score_positive", nullable=False)
        op.alter_column("messages", "score_negative", nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "messages",
        sa.Column("score", sa.Float(), nullable=True),
    )

    op.execute(
        """
        UPDATE messages
        SET score = score_positive
    """
    )

    op.drop_column("messages", "score_positive")
    op.drop_column("messages", "score_negative")

    if op.get_bind().dialect.name != "sqlite":
        op.alter_column("messages", "score", nullable=False)
