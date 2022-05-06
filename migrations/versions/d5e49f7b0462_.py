"""empty message

Revision ID: d5e49f7b0462
Revises: 0f3f21bb0579
Create Date: 2022-05-05 10:41:11.924525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5e49f7b0462'
down_revision = '0f3f21bb0579'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usernames',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usernames')
    # ### end Alembic commands ###
