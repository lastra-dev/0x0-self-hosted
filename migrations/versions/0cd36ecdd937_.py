"""empty message

Revision ID: 0cd36ecdd937
Revises: None
Create Date: 2016-11-01 05:25:42.691768

"""

# revision identifiers, used by Alembic.
revision = '0cd36ecdd937'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.Unicode(256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sha256', sa.Unicode(256), nullable=True),
    sa.Column('ext', sa.Unicode(256), nullable=True),
    sa.Column('mime', sa.Unicode(256), nullable=True),
    sa.Column('addr', sa.Unicode(256), nullable=True),
    sa.Column('removed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sha256')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    op.drop_table('URL')
    ### end Alembic commands ###
