"""remove columns from cheeses

Revision ID: 5715a3e45d42
Revises: e8bd64e1b9f1
Create Date: 2023-08-17 21:54:44.599853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5715a3e45d42'
down_revision = 'e8bd64e1b9f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cheeses', schema=None) as batch_op:
        batch_op.drop_column('is_artisinal')
        batch_op.drop_column('is_hormone_free')
        batch_op.drop_column('is_organic')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cheeses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_organic', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('is_hormone_free', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('is_artisinal', sa.BOOLEAN(), nullable=True))

    # ### end Alembic commands ###
