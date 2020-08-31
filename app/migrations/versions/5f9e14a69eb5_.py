"""empty message

Revision ID: 5f9e14a69eb5
Revises: b96d7e41be9e
Create Date: 2020-08-31 20:35:57.214990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f9e14a69eb5'
down_revision = 'b96d7e41be9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('img_card', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'img_card')
    # ### end Alembic commands ###