"""add_api_requests_table

Revision ID: f5c853b83d41
Revises: 245b57b274c2
Create Date: 2017-07-04 18:38:45.884199

"""

# revision identifiers, used by Alembic.
revision = 'f5c853b83d41'
down_revision = '245b57b274c2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_requests',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('api_name', sa.String(length=256), nullable=True),
    sa.Column('submit_time', sa.DateTime(), nullable=False),
    sa.Column('user_email', sa.String(length=256), nullable=True),
    sa.Column('user_profile_digest', sa.String(length=128), nullable=True),
    sa.Column('origin', sa.String(length=64), nullable=True),
    sa.Column('team', sa.String(length=64), nullable=True),
    sa.Column('recommendation', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_requests')
    # ### end Alembic commands ###
