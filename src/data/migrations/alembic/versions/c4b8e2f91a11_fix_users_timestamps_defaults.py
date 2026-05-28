"""fix users timestamp defaults

Revision ID: c4b8e2f91a11
Revises: 32c37637be27, 1372cb775cc5
Create Date: 2026-05-28 10:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c4b8e2f91a11"
down_revision: Union[str, Sequence[str], None] = ("32c37637be27", "1372cb775cc5")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if inspector.has_table("users"):
        op.execute("UPDATE users SET created_at = now() WHERE created_at IS NULL")
        op.execute("UPDATE users SET updated_at = now() WHERE updated_at IS NULL")

        op.alter_column(
            "users",
            "created_at",
            existing_type=sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
        )
        op.alter_column(
            "users",
            "updated_at",
            existing_type=sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
        )


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if inspector.has_table("users"):
        op.alter_column(
            "users",
            "updated_at",
            existing_type=sa.DateTime(),
            nullable=False,
            server_default=None,
        )
        op.alter_column(
            "users",
            "created_at",
            existing_type=sa.DateTime(),
            nullable=False,
            server_default=None,
        )
