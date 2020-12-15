"""create test view

Revision ID: c633a543c3aa
Revises: 432009cc4e27
Create Date: 2020-12-14 16:43:15.193522

"""
from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_view import PGView


# revision identifiers, used by Alembic.
revision = 'c633a543c3aa'
down_revision = '432009cc4e27'
branch_labels = None
depends_on = None


def upgrade():
    first_view = PGView(
        schema="alembic_test",
        signature="first_view",
        definition="select * from information_schema.tables",
    )

    op.create_entity(first_view)


def downgrade():
    first_view = PGView(
        schema="alembic_test",
        signature="first_view",
        definition="select * from information_schema.tables",
    )

    op.drop_entity(first_view)
