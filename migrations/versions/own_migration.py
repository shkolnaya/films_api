"""added new version

Revision ID: 5950ebb63cfa
Revises: 0b3af8141af4
Create Date: 2022-05-03 14:56:12.499750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = '5950ebb63cfb'
down_revision = '5950ebb63cfa'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%twighlight%'
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%twighlight%'
            """
        )
    )
