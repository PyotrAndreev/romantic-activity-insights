"""Changed chat_id type in TgGroupMessages

Revision ID: 9ea2374d137c
Revises: 8e091062e15b
Create Date: 2024-11-22 23:37:40.234755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ea2374d137c'
down_revision: Union[str, None] = '8e091062e15b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tg_groups_messages', 'tg_groups_stats_last', ['chat_id'], ['chat_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tg_groups_messages', type_='foreignkey')
    # ### end Alembic commands ###
