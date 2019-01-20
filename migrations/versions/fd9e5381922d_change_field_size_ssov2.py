"""change_field_size_ssov2

Revision ID: fd9e5381922d
Revises: 71707fb4716f
Create Date: 2018-11-15 10:53:14.153041

"""

# revision identifiers, used by Alembic.
revision = 'fd9e5381922d'
down_revision = '71707fb4716f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token_scope', 'access_token',
               existing_type=sa.String(length=100),
               type_=sa.String(length=4096))
    op.alter_column('token_scope', 'scope',
               existing_type=sa.String(length=100),
               type_=sa.String(length=250))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token_scope', 'access_token',
               existing_type=sa.String(length=4096),
               type_=sa.String(length=100))
    op.alter_column('token_scope', 'scope',
               existing_type=sa.String(length=250),
               type_=sa.String(length=100))
    # ### end Alembic commands ###
