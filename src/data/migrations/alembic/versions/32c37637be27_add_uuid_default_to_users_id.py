"""add uuid default to users id

Revision ID: 32c37637be27
Revises: 
Create Date: 2026-05-19 05:48:10.712507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32c37637be27'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    op.alter_column(
        "users",
        "id",
        existing_type=sa.UUID(as_uuid=True),
        server_default=sa.text("gen_random_uuid()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "id",
        existing_type=sa.UUID(as_uuid=True),
        server_default=None,
        existing_nullable=False,
    )
