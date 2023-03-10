"""empty message

Revision ID: a7eb5f82921e
Revises: 9906b97e8a85
Create Date: 2023-02-28 04:23:29.311546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7eb5f82921e'
down_revision = '9906b97e8a85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('game', 'description',
               existing_type=sa.VARCHAR(length=400),
               type_=sa.String(length=800),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('game', 'description',
               existing_type=sa.String(length=800),
               type_=sa.VARCHAR(length=400),
               existing_nullable=True)
    # ### end Alembic commands ###
