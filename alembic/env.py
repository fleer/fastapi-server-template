"""Alembic configuration."""

from logging.config import fileConfig

from service.database.database import (
    create_database_with_schema_if_not_exists,
    get_connection_string,
    get_schema,
)
from service.database.models import Base
from sqlalchemy import create_engine, pool

from alembic import context

# Include non-default schemas
context.include_schemas = True


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def create_schema() -> None:
    """Create schema if not exists."""
    url = get_connection_string()
    engine = create_engine(url)
    create_database_with_schema_if_not_exists(engine, get_schema())


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_connection_string()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema=get_schema(),
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    url = get_connection_string()
    connectable = create_engine(url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema=get_schema(),
        )

        with context.begin_transaction():
            context.run_migrations()


create_schema()
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
