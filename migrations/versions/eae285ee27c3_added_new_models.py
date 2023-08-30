"""Added new models

Revision ID: eae285ee27c3
Revises: 
Create Date: 2023-08-29 19:07:23.715706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eae285ee27c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('event_name', sa.String(length=50), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('event_name')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('net_id', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('net_id')
    )
    op.create_table('signup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('signup')
    op.drop_table('member')
    op.drop_table('event')
    # ### end Alembic commands ###
