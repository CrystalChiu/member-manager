"""add_signup_deadline_to_event

Revision ID: f88fa872610c
Revises: eb3bf0bd0a37
Create Date: 2023-09-12 19:53:44.430993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f88fa872610c'
down_revision = 'eb3bf0bd0a37'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('event', sa.Column('signup_deadline', sa.Date(), nullable=True))


def downgrade():
    op.drop_column('event', 'signup_deadline')