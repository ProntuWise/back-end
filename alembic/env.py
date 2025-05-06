from logging.config import fileConfig
import os

from dotenv import load_dotenv
from alembic import context

from scripts.models_registry import Base
from scripts.session import engine  # seu engine customizado com SSL

load_dotenv()

# Caminho absoluto do certificado SSL
caminho = './scripts/ca.pem'
caminho_completo = os.path.abspath(os.path.join(os.getcwd(), caminho))

# Configuração do Alembic
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("AIVEN_URL"))

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData para autogenerate
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa as migrações no modo offline (gera SQL)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa as migrações no modo online (aplica no banco)."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # detecta alterações em tipos
            compare_server_default=True  # detecta mudanças de default
        )

        with context.begin_transaction():
            context.run_migrations()

# Seleciona modo de execução
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
