"""empty message

Revision ID: 9b60fde53474
Revises: 3766ec0f3cd6
Create Date: 2024-04-24 18:58:21.792425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b60fde53474'
down_revision = '3766ec0f3cd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('APP_USER', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight', sa.String(length=8), nullable=True))
        batch_op.add_column(sa.Column('waist_circumference', sa.String(length=8), nullable=True))
        batch_op.add_column(sa.Column('height', sa.String(length=8), nullable=True))
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('APP_USER', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('height')
        batch_op.drop_column('waist_circumference')
        batch_op.drop_column('weight')

    # ### end Alembic commands ###
