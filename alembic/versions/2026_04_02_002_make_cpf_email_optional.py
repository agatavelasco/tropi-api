"""make cpf and email optional on cliente

Revision ID: 002
Revises: 001
Create Date: 2026-04-02
"""
from typing import Sequence, Union
from alembic import op


revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE cliente ALTER COLUMN cpf DROP NOT NULL")
    op.execute("ALTER TABLE cliente ALTER COLUMN email DROP NOT NULL")
    op.execute("ALTER TABLE cliente DROP CONSTRAINT IF EXISTS cliente_cpf_key")
    op.execute("ALTER TABLE cliente DROP CONSTRAINT IF EXISTS cliente_email_key")


def downgrade() -> None:
    op.execute("UPDATE cliente SET cpf = 'N/A_' || id WHERE cpf IS NULL")
    op.execute("UPDATE cliente SET email = 'unknown_' || id || '@placeholder.com' WHERE email IS NULL")
    op.execute("ALTER TABLE cliente ALTER COLUMN cpf SET NOT NULL")
    op.execute("ALTER TABLE cliente ALTER COLUMN email SET NOT NULL")
    op.execute("ALTER TABLE cliente ADD CONSTRAINT cliente_cpf_key UNIQUE (cpf)")
    op.execute("ALTER TABLE cliente ADD CONSTRAINT cliente_email_key UNIQUE (email)")
