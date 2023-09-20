"""add pay_period_id column to member and create pivot table

Revision ID: fd4149665d7d
Revises: 614957861fb1
Create Date: 2023-09-19 18:35:18.042926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd4149665d7d'
down_revision = '614957861fb1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('payment_plan',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('pay_period', sa.String(20), nullable=False),
        sa.Column('price', sa.Float(), nullable=False)
    )   

    op.execute("INSERT INTO payment_plan (id, pay_period, price) VALUES (1, 'quarter', 7)")
    op.execute("INSERT INTO payment_plan (id, pay_period, price) VALUES (2, 'year', 15)")

    with op.batch_alter_table('member') as batch_op:
       batch_op.add_column(sa.Column('payment_plan_id', sa.Integer, sa.ForeignKey('payment_plan.id', name='fk_member_payment_plan'), nullable=True))

def downgrade():
    with op.batch_alter_table('member') as batch_op:
        batch_op.drop_constraint('fk_member_payment_plan')

    op.drop_table('payment_plan')
