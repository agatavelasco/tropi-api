"""
Alembic Environment Configuration — Tropi API

Este arquivo configura o Alembic para:
- Ler a DATABASE_URL do .env (ao inves de usar o valor fixo do alembic.ini)
- Importar todos os models para que o autogenerate funcione
- Suportar migracao online (com conexao ao banco) e offline (gera SQL puro)
"""

import os
import sys
from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import create_engine, pool

# Garante que o diretorio raiz do projeto esta no sys.path
# para que 'from app.xxx' funcione corretamente
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Carrega variaveis de ambiente do .env
load_dotenv()

# Importa a Base e todos os models
# E ESSENCIAL importar os models aqui para que o autogenerate detecte as tabelas
from app.database import Base  # noqa: E402
from app import models  # noqa: E402  — garante que os models sao registrados na Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Le a DATABASE_URL diretamente do .env
# (nao usamos config.set_main_option pois o % na URL causa erro no configparser)
database_url = os.getenv("DATABASE_URL")

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# O metadata da Base contem todos os models registrados.
# E o que o Alembic usa para comparar o estado do banco vs. o estado do codigo.
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    Gera SQL puro sem conectar ao banco. Util para gerar scripts de migracao
    que serao executados manualmente (ex: por um DBA).
    """
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    Conecta ao banco e executa as migracoes diretamente.
    Este e o modo padrao quando voce roda 'alembic upgrade head'.
    """
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
