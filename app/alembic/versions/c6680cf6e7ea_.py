"""empty message

Revision ID: c6680cf6e7ea
Revises: 60db3e457be0
Create Date: 2023-01-20 15:17:10.008771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6680cf6e7ea'
down_revision = '60db3e457be0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('semesters_activities',
    sa.Column('semester_id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.id'], ),
    sa.ForeignKeyConstraint(['semester_id'], ['semesters.id'], ),
    sa.PrimaryKeyConstraint('semester_id', 'activity_id')
    )
    op.create_foreign_key(None, 'courses', 'activities', ['id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'courses', type_='foreignkey')
    op.drop_table('semesters_activities')
    # ### end Alembic commands ###
