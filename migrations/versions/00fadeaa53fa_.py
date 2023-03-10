"""empty message

Revision ID: 00fadeaa53fa
Revises: f26b58e3a192
Create Date: 2023-02-21 04:28:22.538095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00fadeaa53fa'
down_revision = 'f26b58e3a192'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_tags',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'user_id')
    )
    op.add_column('comment', sa.Column('score', sa.Integer(), nullable=False))
    op.alter_column('comment', 'content',
               existing_type=sa.VARCHAR(length=400),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'content',
               existing_type=sa.VARCHAR(length=400),
               nullable=False)
    op.drop_column('comment', 'score')
    op.drop_table('user_tags')
    # ### end Alembic commands ###
