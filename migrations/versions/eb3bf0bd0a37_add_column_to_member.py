"""add column to member

Revision ID: eb3bf0bd0a37
Revises: eae285ee27c3
Create Date: 2023-09-05 16:53:19.351569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb3bf0bd0a37'
down_revision = 'eae285ee27c3'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('member', sa.Column('attendance', sa.Integer(), default=0))

def downgrade():
    op.drop_column('member', 'attendance')