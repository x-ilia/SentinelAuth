"""create account table

Revision ID: 4f90f46c9ac8
Revises: 
Create Date: 2025-02-12 20:40:31.365870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f90f46c9ac8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name',  sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')