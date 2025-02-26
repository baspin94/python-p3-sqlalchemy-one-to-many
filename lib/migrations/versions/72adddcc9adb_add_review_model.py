"""Add Review model

Revision ID: 72adddcc9adb
Revises: c8957c5c56d7
Create Date: 2023-03-07 12:20:38.166862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72adddcc9adb'
down_revision = 'c8957c5c56d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
