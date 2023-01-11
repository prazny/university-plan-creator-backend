"""create_opinions_table

Revision ID: 9d02797eaad3
Revises: f69773b1fa4e
Create Date: 2023-01-11 19:45:38.260526

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9d02797eaad3'
down_revision = 'f69773b1fa4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('opinions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('is_approved', sa.Boolean(), nullable=False),
                    sa.Column('description', sa.String(length=50), nullable=False),
                    sa.Column('status', sa.Enum('Positive', 'Negative', name='opinion_status'), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_opinions_id'), 'opinions', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_opinions_id'), table_name='opinions')
    op.drop_table('opinions')
