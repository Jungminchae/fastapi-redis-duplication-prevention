"""Create Vote Table

Revision ID: 33b44632669c
Revises: 
Create Date: 2024-04-01 17:13:00.255982

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "33b44632669c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "votes",
        sa.Column("id", sa.Integer, primary_key=True, index=True, autoincrement=True),
        sa.Column("user_id", sa.Integer),
        sa.Column("candidate_id", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("votes")
