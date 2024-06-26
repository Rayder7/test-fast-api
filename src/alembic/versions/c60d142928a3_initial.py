"""initial

Revision ID: c60d142928a3
Revises: 
Create Date: 2024-06-26 22:10:29.235634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c60d142928a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status_closure', sa.Boolean(), nullable=False),
    sa.Column('task_representation', sa.String(), nullable=False),
    sa.Column('line', sa.String(), nullable=False),
    sa.Column('shift', sa.String(), nullable=False),
    sa.Column('team', sa.String(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.Column('batch_date', sa.Date(), nullable=False),
    sa.Column('nomenclature', sa.String(), nullable=True),
    sa.Column('ekn_code', sa.String(), nullable=True),
    sa.Column('rc_identifier', sa.String(), nullable=True),
    sa.Column('start_datetime', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('end_datetime', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('batch_id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unique_code', sa.Integer(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.Column('batch_date', sa.Date(), nullable=False),
    sa.Column('is_aggregated', sa.Boolean(), nullable=False),
    sa.Column('aggregated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['batch_id'], ['batches.batch_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unique_code')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('batches')
    # ### end Alembic commands ###
