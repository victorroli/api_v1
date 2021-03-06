"""Correção de campos na tabela Experimentos

Revision ID: 53ae2cb2a02c
Revises: f6824efd71aa
Create Date: 2019-08-08 22:32:44.305466

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '53ae2cb2a02c'
down_revision = 'f6824efd71aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
#    op.add_column('experimentos', sa.Column('periodo_fim', sa.DateTime(), nullable=True))
 #   op.add_column('experimentos', sa.Column('periodo_inicio', sa.DateTime(), nullable=False))
    op.alter_column('experimentos', 'periodo_fim',
               existing_type=sa.DateTime(),
               nullable=True)

  #  op.drop_column('experimentos', 'periodoInicio')
  #  op.drop_column('experimentos', 'periodoFim')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experimentos', sa.Column('periodoFim', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('experimentos', sa.Column('periodoInicio', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('experimentos', 'periodo_inicio')
    op.drop_column('experimentos', 'periodo_fim')
    # ### end Alembic commands ###
