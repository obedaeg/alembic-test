"""create account table

Revision ID: 0bc607352654
Revises: 
Create Date: 2020-12-14 14:02:08.766208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey, MetaData

revision = '0bc607352654'
down_revision = None
branch_labels = None
depends_on = None

metadata = MetaData(schema="alembic_test")

def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True, redshift_encode='az64'),
        sa.Column('name', sa.String(50), nullable=False, redshift_encode='zstd'),
        sa.Column('description', sa.String(100), redshift_encode='zstd'),
        redshift_diststyle='Key',
        redshift_distkey='id',
        redshift_interleaved_sortkey=['id', 'name']
    )


def downgrade():
    op.drop_table('account')
