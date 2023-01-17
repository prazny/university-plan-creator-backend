"""create users table

Revision ID: ca460f426297
Revises: 5051a4857df2
Create Date: 2023-01-17 17:10:21.968921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca460f426297'
down_revision = '5051a4857df2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('login', sa.String(length=30), nullable=False),
                    sa.Column('email', sa.String(length=30), nullable=False),
                    sa.Column('password', sa.String(length=30), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
