"""empty message

Revision ID: ec13d13e9925
Revises: f1b178de0356
Create Date: 2023-07-19 09:32:46.155510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec13d13e9925'
down_revision = 'f1b178de0356'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_added')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_added', sa.DATETIME(), nullable=False))

    # ### end Alembic commands ###
