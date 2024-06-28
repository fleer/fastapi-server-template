"""Database configuration.

Load the database configuration and manage the connection to the database.

Provides functions for creating the connection string
and creating the database with the given schema if it not exists.
"""

import logging

import sqlalchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from service.utils import get_config

logger = logging.getLogger(__name__)


def get_schema() -> str:
    """Get the schema from the config file.

    Returns:
    -------
        str: Schema name
    """
    full_config = get_config()
    return full_config.database.db_schema


def get_connection_string() -> str:
    """Create URI for database access.

    Function for reading the given section of a config file

    Raises:
    ------
        Exception: Section not found

    Returns:
    -------
        str: Connection string
        str: Schema (default: public)
    """
    connection_info = get_config().database
    logger.debug("Establish database connection...")
    for attribute, value in connection_info.__dict__.items():
        if attribute != "password":
            logger.debug("Parameter - %s: %s", attribute, value)
    return (
        f"postgresql+psycopg://{connection_info.user}:"
        + f"{connection_info.password}@"
        + f"{connection_info.host}:{connection_info.port}"
        + f"/{connection_info.db_name}"
    )


def create_database_with_schema_if_not_exists(
    engine: sqlalchemy.engine.Engine, schema: str, reset_schema: bool = False
) -> None:
    """Intialization function for database.

    Manage the creation of the database and schema.

    Args:
        engine (Engine): Database engine
        schema (str): Used schema
        reset_schema (bool): Should the schema be cleared.
    """
    inspector = sqlalchemy.inspect(engine)
    if not database_exists(engine.url):
        # WARNING This does not work as long as db is in engine path
        create_database(engine.url)
    if reset_schema:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(
                    sqlalchemy.schema.DropSchema(schema, cascade=True, if_exists=True)
                )
    if not inspector.has_schema(schema_name=schema):
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(sqlalchemy.schema.CreateSchema(schema))


SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=create_engine(get_connection_string())
)

metadata = MetaData(schema=get_schema())
