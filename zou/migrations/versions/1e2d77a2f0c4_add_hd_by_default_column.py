"""Add is hd_by_default column to organisation table

Revision ID: 1e2d77a2f0c4
Revises: 4e3738cdc34c
Create Date: 2021-10-12 18:56:43.683008

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '1e2d77a2f0c4'
down_revision = '4e3738cdc34c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organisation', sa.Column('hd_by_default', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organisation', 'hd_by_default')
    # ### end Alembic commands ###