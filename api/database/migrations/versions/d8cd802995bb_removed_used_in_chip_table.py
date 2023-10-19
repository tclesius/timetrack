"""removed used in chip table

Revision ID: d8cd802995bb
Revises: 36ad83cd0534
Create Date: 2023-10-19 21:20:43.508442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8cd802995bb'
down_revision: Union[str, None] = '36ad83cd0534'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chip', 'used')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chip', sa.Column('used', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###