"""create tables

Revision ID: e8bd64e1b9f1
Revises: 
Create Date: 2023-08-17 21:10:35.305861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8bd64e1b9f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('founding_year', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('operation_size', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cheeses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(), nullable=True),
    sa.Column('is_organic', sa.Boolean(), nullable=True),
    sa.Column('is_raw_milk', sa.Boolean(), nullable=True),
    sa.Column('is_artisinal', sa.Boolean(), nullable=True),
    sa.Column('is_hormone_free', sa.Boolean(), nullable=True),
    sa.Column('production_date', sa.DateTime(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('producer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['producer_id'], ['producers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cheeses')
    op.drop_table('producers')
    # ### end Alembic commands ###
