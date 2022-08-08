"""empty message

Revision ID: 831498f2d18e
Revises: 
Create Date: 2022-07-31 02:12:12.114637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '831498f2d18e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gems', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('expirience', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'expirience')
    op.drop_column('user', 'gems')
    # ### end Alembic commands ###
