"""create students table

Revision ID: 720b74e4aa67
Revises: a0808753fada
Create Date: 2024-03-21 23:56:36.935199

"""
from random import choice
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '720b74e4aa67'
down_revision: Union[str, None] = 'a0808753fada'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def random_classroom_id() -> int:
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def random_student_code() -> str:
    # Generate a random student code
    return ''.join(choice('0123456789') for _ in range(9))

def upgrade() -> None:
    students_table = op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('student_code', sa.String(9), nullable=False, unique=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('birthdate', sa.Date, nullable=False),
        sa.Column('email', sa.String(200), nullable=False, unique=True),
        sa.Column('phone', sa.String(15), nullable=False),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classrooms.id'), nullable=True)
    )

    op.bulk_insert(
        students_table,
        [
            {'student_code': random_student_code(), 'first_name': 'Juan', 'last_name': 'Pérez', 'birthdate': '2005-05-10', 'email': 'juanperez@example.com', 'phone': '555-1234', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'María', 'last_name': 'Gómez', 'birthdate': '2006-02-15', 'email': 'mariagomez@example.com', 'phone': '555-5678', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Carlos', 'last_name': 'Martínez', 'birthdate': '2005-11-20', 'email': 'carlosmartinez@example.com', 'phone': '555-9012', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Ana', 'last_name': 'López', 'birthdate': '2006-07-03', 'email': 'analopez@example.com', 'phone': '555-3456', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Pedro', 'last_name': 'Rodríguez', 'birthdate': '2005-09-28', 'email': 'pedrorodriguez@example.com', 'phone': '555-7890', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Laura', 'last_name': 'Hernández', 'birthdate': '2006-04-12', 'email': 'laurahernandez@example.com', 'phone': '555-2345', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Javier', 'last_name': 'Díaz', 'birthdate': '2005-12-08', 'email': 'javierdiaz@example.com', 'phone': '555-6789', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Lucía', 'last_name': 'García', 'birthdate': '2006-08-17', 'email': 'luciagarcia@example.com', 'phone': '555-1234', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Diego', 'last_name': 'Sánchez', 'birthdate': '2005-10-25', 'email': 'diegosanchez@example.com', 'phone': '555-5678', 'classroom_id': random_classroom_id()},
            {'student_code': random_student_code(), 'first_name': 'Sofía', 'last_name': 'Pérez', 'birthdate': '2006-03-31', 'email': 'sofiaperez@example.com', 'phone': '555-9012', 'classroom_id': random_classroom_id()},
        ]
    )


def downgrade() -> None:
    op.drop_table('students')
