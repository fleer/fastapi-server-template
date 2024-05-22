"""Database configuration."""

import logging
import os
from typing import Tuple

import sqlalchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from ..config import CONFIG_DIR
from ..utils import get_config

logger = logging.getLogger(__name__)


def config(filename: str = CONFIG_DIR, stage: str | None = None) -> Tuple[str, str]:
    """config.

    Function for reading the given section of a config file

    Args:
        filename (str, optional): Filename of the config file in root folder.
        from_env (boolean, optional): Fetch values from ENV variable,
                                      if exists

    Raises:
    ------
        Exception: Section not found

    Returns:
    -------
        str: Connection string
        str: Schema (default: public)
    """
    logger.debug(filename)
    full_config = get_config(filename)
    if stage is None:
        stage = os.getenv("stage", "dev")
    data_base = {}
    if stage in full_config["connection"].keys():
        connection_info = full_config["connection"][stage]
        # get section, default to postgresql
        params = connection_info.items()
        for param in params:
            key = param[0]
            value = param[1]
            data_base[key] = value
            if key != "password":
                logger.debug("Parameter - %s: %s", key, data_base[key])
    else:
        raise Exception("Connection not found in config file.")
    return (
        f"postgresql+psycopg://{data_base['user']}:"
        + f"{data_base['password']}@"
        + f"{data_base['host']}:{data_base['port']}"
        + f"/{data_base['dbname']}"
    ), data_base.get("schema", "public")


def create_database_with_schema_if_not_exists(
    engine: sqlalchemy.engine.Engine, schema: str, reset_schema: bool = False
) -> None:
    """Intialization function for database.

    Manage the creation of the database and schema.

    Args:
        engine: Database engine
        schema: Used schema
        reset_schema: Should the schema be cleared.
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


connection_string, schema = config()
engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData(schema=schema)

Base = declarative_base(metadata=metadata)
