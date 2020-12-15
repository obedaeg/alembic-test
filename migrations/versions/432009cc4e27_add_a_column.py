"""Add a column

Revision ID: 432009cc4e27
Revises: 0bc607352654
Create Date: 2020-12-14 14:37:38.930952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import MetaData

revision = '432009cc4e27'
down_revision = '0bc607352654'
branch_labels = None
depends_on = None

metadata = MetaData(schema="alembic_test")

def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
