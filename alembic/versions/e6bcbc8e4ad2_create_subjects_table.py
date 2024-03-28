"""create subjects table

Revision ID: e6bcbc8e4ad2
Revises: 
Create Date: 2024-03-21 22:38:49.800865

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6bcbc8e4ad2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    subjects_table = op.create_table(
        'subjects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('description', sa.String(200))
    )

    op.bulk_insert(
        subjects_table,
        [
            {'name': 'Matemáticas', 'description': 'Clase que abarca conceptos de aritmética, álgebra, geometría, trigonometría y cálculo.'},
            {'name': 'Ciencias Naturales', 'description': 'Estudio de los fenómenos naturales, incluyendo biología, química, física, y astronomía.'},
            {'name': 'Lengua y Literatura', 'description': 'Enseñanza de gramática, composición escrita, análisis literario y apreciación de la literatura.'},
            {'name': 'Historia', 'description': 'Estudio de los eventos pasados y su impacto en la sociedad, la cultura y el mundo actual.'},
            {'name': 'Educación Física', 'description': 'Clase enfocada en actividades físicas para promover la salud y el bienestar.'},
            {'name': 'Artística', 'description': 'Exploración de diversas formas de expresión artística, como pintura, música, teatro y danza.'},
            {'name': 'Inglés', 'description': 'Aprendizaje del idioma inglés como segunda lengua, incluyendo gramática, vocabulario y conversación.'},
            {'name': 'Cívica y Ética', 'description': 'Instrucción sobre los derechos y deberes de los ciudadanos, así como valores éticos y morales.'},
            {'name': 'Tecnología', 'description': 'Clase que cubre temas relacionados con la informática, la programación, la robótica y la tecnología en general.'},
            {'name': 'Salud y Bienestar', 'description': 'Enseñanza sobre hábitos saludables, prevención de enfermedades y promoción del bienestar físico y mental.'}
        ]
    )


def downgrade() -> None:
    pass
