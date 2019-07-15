"""empty message

Revision ID: 3f21e107bd02
Revises: 62c6ce8d29ae
Create Date: 2019-07-14 18:09:23.574242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f21e107bd02'
down_revision = '62c6ce8d29ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('laboratorios_laboratorio_id_fkey', 'laboratorios', type_='foreignkey')
    op.drop_column('laboratorios', 'uri')
    op.drop_column('laboratorios', 'laboratorio_id')
    op.drop_column('laboratorios', 'nome')
    op.drop_column('laboratorios', 'descricao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('laboratorios', sa.Column('descricao', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('laboratorios', sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('laboratorios', sa.Column('laboratorio_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('laboratorios', sa.Column('uri', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('laboratorios_laboratorio_id_fkey', 'laboratorios', 'laboratorios', ['laboratorio_id'], ['id'])
    # ### end Alembic commands ###
