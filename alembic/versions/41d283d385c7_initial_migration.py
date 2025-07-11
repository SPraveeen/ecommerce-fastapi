"""Initial migration

Revision ID: 41d283d385c7
Revises: 
Create Date: 2025-06-15 16:15:45.296909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41d283d385c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('role', sa.Enum('admin', 'customer', 'staff', name='user_roles'), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('locale', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('email_validated', sa.Boolean(), nullable=True),
    sa.Column('phone_validated', sa.Boolean(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
