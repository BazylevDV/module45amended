"""empty message

Revision ID: aea879e12bce
Revises: 1c5bb642b78b
Create Date: 2024-12-12 15:03:17.658620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aea879e12bce'
down_revision: Union[str, None] = '1c5bb642b78b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
