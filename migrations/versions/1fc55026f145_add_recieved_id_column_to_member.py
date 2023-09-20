"""add recieved_id column to member

Revision ID: 1fc55026f145
Revises: 53d92a1019b4
Create Date: 2023-09-19 17:21:53.640063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc55026f145'
down_revision = '53d92a1019b4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('member', sa.Column('received_id', sa.Boolean(), default=False))


def downgrade():
    op.drop_column('member', 'received_id')