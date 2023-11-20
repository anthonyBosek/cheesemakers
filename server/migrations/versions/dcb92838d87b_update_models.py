"""update models

Revision ID: dcb92838d87b
Revises: 1f2cb217cb51
Create Date: 2023-11-20 07:46:56.283652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcb92838d87b'
down_revision = '1f2cb217cb51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cheeses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.alter_column('kind',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('is_raw_milk',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=True)

    with op.batch_alter_table('producers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.alter_column('founding_year',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('region',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('operation_size',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('producers', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('operation_size',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('region',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('founding_year',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('cheeses', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('is_raw_milk',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('kind',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###