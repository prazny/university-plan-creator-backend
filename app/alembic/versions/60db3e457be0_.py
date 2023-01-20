"""empty message

Revision ID: 60db3e457be0
Revises: 9d02797eaad3
Create Date: 2023-01-17 17:47:35.221445

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60db3e457be0'
down_revision = '9d02797eaad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plan_semester')
    op.drop_index('ix_opinions_id', table_name='opinions')
    op.drop_table('opinions')
    op.add_column('semesters', sa.Column('plan_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'semesters', 'plans', ['plan_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'semesters', type_='foreignkey')
    op.drop_column('semesters', 'plan_id')
    op.create_table('opinions',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('is_approved', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('description', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('status', mysql.ENUM('positive', 'negative'), nullable=True),
    sa.Column('user', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('plan', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_opinions_id', 'opinions', ['id'], unique=False)
    op.create_table('plan_semester',
    sa.Column('semester_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('plan_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['plan_id'], ['plans.id'], name='plan_semester_ibfk_1'),
    sa.ForeignKeyConstraint(['semester_id'], ['semesters.id'], name='plan_semester_ibfk_2'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###