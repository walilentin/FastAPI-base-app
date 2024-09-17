"""2

Revision ID: 193f5c0d3e7b
Revises: 652fbef569e7
Create Date: 2024-09-13 12:58:09.595007

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "193f5c0d3e7b"
down_revision: Union[str, None] = "652fbef569e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("foo", sa.Integer(), nullable=False),
        sa.Column("bar", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
        sa.UniqueConstraint("foo", "bar", name=op.f("uq_user_foo")),
        sa.UniqueConstraint("username", name=op.f("uq_user_username")),
    )


def downgrade() -> None:
    op.drop_table("user")
