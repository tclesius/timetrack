"""renamed token to pairing_token in chip table

Revision ID: 59eb1f713b82
Revises: d8cd802995bb
Create Date: 2023-10-19 21:34:25.225171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59eb1f713b82'
down_revision: Union[str, None] = 'd8cd802995bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chip', sa.Column('pairing_token', sa.String(length=8), nullable=False))
    op.drop_constraint('chip_token_key', 'chip', type_='unique')
    op.create_unique_constraint(None, 'chip', ['pairing_token'])
    op.drop_column('chip', 'token')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chip', sa.Column('token', sa.VARCHAR(length=8), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'chip', type_='unique')
    op.create_unique_constraint('chip_token_key', 'chip', ['token'])
    op.drop_column('chip', 'pairing_token')
    # ### end Alembic commands ###
