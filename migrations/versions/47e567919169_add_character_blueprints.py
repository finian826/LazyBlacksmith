"""add character blueprints

Revision ID: 47e567919169
Revises: 02bf73d552c2
Create Date: 2017-04-12 00:26:03.535000

"""

# revision identifiers, used by Alembic.
revision = '47e567919169'
down_revision = '02bf73d552c2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blueprint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.BigInteger(), nullable=True),
    sa.Column('original', sa.Boolean(), nullable=False),
    sa.Column('total_runs', sa.Integer(), nullable=False),
    sa.Column('material_efficiency', sa.Integer(), nullable=False),
    sa.Column('time_efficiency', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['user.character_id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blueprint')
    # ### end Alembic commands ###
