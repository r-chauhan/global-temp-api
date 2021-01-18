"""empty message

Revision ID: a1e2903c842a
Revises: 
Create Date: 2021-01-16 22:33:45.581576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1e2903c842a'
down_revision = None
branch_labels = None
depends_on = None


# seq_id = Sequence('seq_id', start=1, increment=1)


def upgrade():
    op.create_table('Global_Land_Temperatures_By_City',
    sa.Column('id', sa.BigInteger(), nullable=False, autoincrement=True),
    sa.Column('dt', sa.Date(), nullable=True),
    sa.Column('AverageTemperature', sa.Numeric(), nullable=True),
    sa.Column('AverageTemperatureUncertainty', sa.Numeric(), nullable=True),
    sa.Column('City', sa.String(), nullable=True),
    sa.Column('Country', sa.String(), nullable=True),
    sa.Column('Latitude', sa.String(), nullable=True),
    sa.Column('Longitude', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )


def downgrade():
    op.drop_table('Global_Land_Temperatures_By_City')
