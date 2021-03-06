"""Adição de campo na tabela Experimento

Revision ID: 26c5baf21c52
Revises: 057e4148f117
Create Date: 2019-07-23 00:03:57.977230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26c5baf21c52'
down_revision = ''
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experimentos', sa.Column('observacao', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('experimentos', 'observacao')
    # ### end Alembic commands ###
