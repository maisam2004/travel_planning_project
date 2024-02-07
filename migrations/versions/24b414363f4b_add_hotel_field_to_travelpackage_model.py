"""Add hotel field to TravelPackage model

Revision ID: 24b414363f4b
Revises: 93acde3c0db3
Create Date: 2024-02-07 13:44:51.509183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24b414363f4b'
down_revision = '93acde3c0db3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travel_package', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travel_package', schema=None) as batch_op:
        batch_op.drop_column('hotel')

    # ### end Alembic commands ###
