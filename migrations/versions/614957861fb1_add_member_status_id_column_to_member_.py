"""add member_status_id column to member and create pivot table

Revision ID: 614957861fb1
Revises: 1fc55026f145
Create Date: 2023-09-19 18:07:16.934043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '614957861fb1'
down_revision = '1fc55026f145'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('member_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String(20), nullable=False)
    )   

    op.execute("INSERT INTO member_status (id, status) VALUES (1, 'free')")
    op.execute("INSERT INTO member_status (id, status) VALUES (2, 'paid')")
    op.execute("INSERT INTO member_status (id, status) VALUES (3, 'expired')")

    with op.batch_alter_table('member') as batch_op:
        batch_op.add_column(sa.Column('member_status_id', sa.Integer, sa.ForeignKey('member_status.id', name='fk_member_member_status'), nullable=False, default=1))
        batch_op.drop_column('status')

def downgrade():
    #add status column back to the Member table
    op.add_column('member', sa.Column('status', sa.String(20), nullable=False, default='free'))

    #populate status column with default value 'free'
    op.execute("UPDATE member SET status='free'")


    #remove  member_status_id column from Member table
    with op.batch_alter_table('member') as batch_op:
        batch_op.drop_constraint('fk_member_member_status')

    #drop member_statuses table
    op.drop_table('member_status')
