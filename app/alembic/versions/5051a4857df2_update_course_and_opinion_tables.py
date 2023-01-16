"""update course and opinion tables

Revision ID: 5051a4857df2
Revises: 9d02797eaad3
Create Date: 2023-01-12 19:42:48.633623

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5051a4857df2'
down_revision = '9d02797eaad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # course
    op.drop_table("courses")
    op.create_table('courses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.Column('ects', sa.Integer(), nullable=False),
                    sa.Column('cnps', sa.Integer(), nullable=False),
                    sa.Column('zzu', sa.Integer(), nullable=False),
                    sa.Column('bu', sa.Integer(), nullable=False),
                    sa.Column('hours_count', sa.Integer(), nullable=False),
                    sa.Column('direction', sa.String(length=50), nullable=False),
                    sa.Column('code', sa.String(length=20), nullable=True),
                    sa.Column('type', sa.Enum('laboratory', 'practice', 'lecture', 'project', 'seminar', 'lang_course',
                                              'thesis', name='type'), nullable=False),
                    sa.Column('completing_form', sa.String(length=50), nullable=True),
                    sa.Column('course_form', sa.Enum('stationary', 'remote', name='form'), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_courses_id'), 'courses', ['id'], unique=False)


def downgrade() -> None:
    pass
