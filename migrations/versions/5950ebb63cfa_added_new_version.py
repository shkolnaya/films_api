"""added new version

Revision ID: 5950ebb63cfa
Revises: 0b3af8141af4
Create Date: 2022-05-03 14:56:12.499750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5950ebb63cfa'
down_revision = '0b3af8141af4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('test', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'test')
    # ### end Alembic commands ###
