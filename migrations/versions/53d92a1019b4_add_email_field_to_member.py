"""add_email_field_to_member

Revision ID: 53d92a1019b4
Revises: f88fa872610c
Create Date: 2023-09-19 16:46:12.330576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d92a1019b4'
down_revision = 'f88fa872610c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('member', sa.Column('email', sa.String(length=50), nullable=False))


def downgrade():
    op.drop_column('member', 'email')
    
