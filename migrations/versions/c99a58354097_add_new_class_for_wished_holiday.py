"""add new class for wished holiday

Revision ID: c99a58354097
Revises: f83ef7dd43bc
Create Date: 2024-02-10 15:28:27.701414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c99a58354097'
down_revision = 'f83ef7dd43bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wished_holiday', schema=None) as batch_op:
        batch_op.alter_column('price_range',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wished_holiday', schema=None) as batch_op:
        batch_op.alter_column('price_range',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
