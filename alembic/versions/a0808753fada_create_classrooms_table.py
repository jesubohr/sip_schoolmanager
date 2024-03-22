"""create classrooms table

Revision ID: a0808753fada
Revises: e6bcbc8e4ad2
Create Date: 2024-03-21 23:33:34.408144

"""
from random import choice
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0808753fada'
down_revision: Union[str, None] = 'e6bcbc8e4ad2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def random_representative() -> int:
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def upgrade() -> None:
    classrooms_table = op.create_table(
        'classrooms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(100)),
        sa.Column('representative', sa.Integer, nullable=False)
    )

    op.bulk_insert(
        classrooms_table,
        [
            {'name': '1A', 'description': 'Salón de primer año A', 'representative': random_representative()},
            {'name': '1B', 'description': 'Salón de primer año B', 'representative': random_representative()},
            {'name': '2A', 'description': 'Salón de segundo año A', 'representative': random_representative()},
            {'name': '2B', 'description': 'Salón de segundo año B', 'representative': random_representative()},
            {'name': '3A', 'description': 'Salón de tercer año A', 'representative': random_representative()},
            {'name': '3B', 'description': 'Salón de tercer año B', 'representative': random_representative()},
            {'name': '4A', 'description': 'Salón de cuarto año A', 'representative': random_representative()},
            {'name': '4B', 'description': 'Salón de cuarto año B', 'representative': random_representative()},
            {'name': '5A', 'description': 'Salón de quinto año A', 'representative': random_representative()},
            {'name': '5B', 'description': 'Salón de quinto año B', 'representative': random_representative()}
        ]
    )


def downgrade() -> None:
    op.drop_table('classrooms')
