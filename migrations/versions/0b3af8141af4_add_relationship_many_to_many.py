"""add relationship many-to-many

Revision ID: 0b3af8141af4
Revises: 51e7646b9961
Create Date: 2022-04-29 15:28:03.100060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3af8141af4'
down_revision = '51e7646b9961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies_actors',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('actor_id', 'film_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    # ### end Alembic commands ###
