"""initial schema — snapshot do estado atual do banco

Revision ID: 001
Revises: None
Create Date: 2026-02-15

Esta migracao representa o estado atual das tabelas (cliente e atendimento)
que ja existem no banco Supabase. Ela foi criada manualmente para que o
Alembic tenha um ponto de partida.

IMPORTANTE: Como as tabelas ja existem, ao rodar 'alembic upgrade head'
pela primeira vez, use 'alembic stamp head' em vez de 'alembic upgrade head'.
Isso marca a migracao como aplicada SEM executar o SQL.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Tabela: cliente
    op.create_table(
        "cliente",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("cpf", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("telefone", sa.String(), nullable=True),
        sa.Column("cep", sa.String(length=9), nullable=True),
        sa.Column("logradouro", sa.String(), nullable=True),
        sa.Column("numero", sa.String(), nullable=True),
        sa.Column("complemento", sa.String(), nullable=True),
        sa.Column("bairro", sa.String(), nullable=True),
        sa.Column("localidade", sa.String(), nullable=True),
        sa.Column("uf", sa.String(length=2), nullable=True),
        sa.Column("estado", sa.String(), nullable=True),
        sa.Column("criado_em", sa.DateTime(), nullable=True),
        sa.Column("atualizado_em", sa.DateTime(), nullable=True),
        sa.UniqueConstraint("cpf"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_cliente_id"), "cliente", ["id"], unique=False)

    # Tabela: atendimento
    op.create_table(
        "atendimento",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("cliente_id", sa.Integer(), sa.ForeignKey("cliente.id"), nullable=False),
        sa.Column("data_hora_inicio", sa.DateTime(), nullable=False),
        sa.Column("data_hora_fim", sa.DateTime(), nullable=False),
        sa.Column("tipo_servico", sa.String(), nullable=False),
        sa.Column("duracao", sa.String(), nullable=False),
        sa.Column("resumo", sa.String(), nullable=False),
        sa.Column("observacoes", sa.String(), nullable=False),
        sa.Column("intervencoes", sa.String(), nullable=False),
        sa.Column("recomendacoes", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("criado_em", sa.DateTime(), nullable=True),
        sa.Column("atualizado_em", sa.DateTime(), nullable=True),
    )
    op.create_index(op.f("ix_atendimento_id"), "atendimento", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_atendimento_id"), table_name="atendimento")
    op.drop_table("atendimento")
    op.drop_index(op.f("ix_cliente_id"), table_name="cliente")
    op.drop_table("cliente")
