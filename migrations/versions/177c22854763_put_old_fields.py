"""put old fields

Revision ID: 177c22854763
Revises: d3da56bdc47a
Create Date: 2024-02-08 13:02:42.558104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '177c22854763'
down_revision = 'd3da56bdc47a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travel_package', schema=None) as batch_op:
        batch_op.drop_column('duration')
        batch_op.drop_column('hotel_description')
        batch_op.drop_column('package_price')
        batch_op.drop_column('icons')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('travel_package', schema=None) as batch_op:
        batch_op.add_column(sa.Column('icons', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('package_price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('hotel_description', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('duration', sa.VARCHAR(length=150), autoincrement=False, nullable=True))

    # ### end Alembic commands ###