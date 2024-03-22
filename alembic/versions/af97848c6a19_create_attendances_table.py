"""create attendances table

Revision ID: af97848c6a19
Revises: 720b74e4aa67
Create Date: 2024-03-22 00:13:48.740826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af97848c6a19'
down_revision: Union[str, None] = '720b74e4aa67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'attendances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=True),
        sa.Column('subject_id', sa.Integer, sa.ForeignKey('subjects.id'), nullable=True),
        sa.Column('attended', sa.Boolean, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('attendances')
