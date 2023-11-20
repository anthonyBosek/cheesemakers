"""initial model setup

Revision ID: 1f2cb217cb51
Revises: 
Create Date: 2023-11-20 07:34:58.351387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f2cb217cb51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.Column('founding_year', sa.Integer(), nullable=False),
    sa.Column('operation_size', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cheeses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(length=50), nullable=False),
    sa.Column('is_raw_milk', sa.Boolean(), nullable=False),
    sa.Column('production_date', sa.DateTime(), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
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
