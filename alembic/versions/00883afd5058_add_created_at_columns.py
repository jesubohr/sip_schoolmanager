"""add created_at columns

Revision ID: 00883afd5058
Revises: af97848c6a19
Create Date: 2024-03-22 00:24:14.513380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00883afd5058'
down_revision: Union[str, None] = 'af97848c6a19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('subjects', sa.Column('created_at', sa.DateTime, server_default=sa.func.now()))
    op.add_column('classrooms', sa.Column('created_at', sa.DateTime, server_default=sa.func.now()))
    op.add_column('students', sa.Column('created_at', sa.DateTime, server_default=sa.func.now()))
    op.add_column('attendances', sa.Column('created_at', sa.DateTime, server_default=sa.func.now()))


def downgrade() -> None:
    op.drop_column('subjects', 'created_at')
    op.drop_column('classrooms', 'created_at')
    op.drop_column('students', 'created_at')
    op.drop_column('attendances', 'created_at')
