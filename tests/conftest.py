"""Configuration for pytest."""

import os
from shutil import copytree
from time import sleep
from typing import Any, Generator
from unittest.mock import patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from service.database import database
from service.routes import healthcheck, tag
from sqlalchemy import create_engine, schema
from sqlalchemy_utils import create_database, database_exists, drop_database

import alembic.config
from alembic.command import upgrade

ALEMBIC_CONFIG = "alembic.ini"


def mock_connection_string() -> str:
    """Mock string for db connection."""
    return "postgresql+psycopg://postgres:postgres@localhost:5432/test"


patch("service.database.database.get_connection_string", mock_connection_string).start()


def migrate_in_memory(
    migrations_path: str,
    alembic_ini_path: str = ALEMBIC_CONFIG,
    revision: str = "head",
) -> None:
    """Migrate the database in memory.

    Args:
        migrations_path: migration path
        alembic_ini_path: path to alembic.ini
        connection: SQLAlchemy connection
        revision: used revision
    """
    config = alembic.config.Config(alembic_ini_path)
    config.set_main_option("script_location", migrations_path)
    upgrade(config, revision)
    # HACK: Add sleep in order to prevent execution of tests befor db upgrade
    sleep(1)


def pytest_sessionstart() -> None:
    """Set up the database."""
    os.environ["STAGE"] = "test"
    url = database.get_connection_string()
    if not database_exists(url):
        create_database(url)


def pytest_sessionfinish() -> None:
    """Delete the database."""
    url = database.get_connection_string()
    if database_exists(url):
        drop_database(url)


@pytest.fixture
def datadir(tmpdir: str, request: pytest.FixtureRequest) -> str:
    """datadir.

    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.

    Args:
        tmpdir (str): temp directory given by pytest
        request: request
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        copytree(test_dir, tmpdir.__str__(), dirs_exist_ok=True)

    return tmpdir


@pytest.fixture(scope="function", autouse=True)
def db_initializer() -> Generator[pytest.Session, Any, None]:
    """Create a fresh database on each test case.

    Use alembic if the config file exists,
    otherwise create the tables directly.

    """
    migrate_in_memory("alembic", ALEMBIC_CONFIG)
    print("\n----- CREATE TEST DB INSTANCE POOL\n")
    yield
    with create_engine(database.get_connection_string()).connect() as connection:
        with connection.begin():
            connection.execute(
                schema.DropSchema(database.get_schema(), cascade=True, if_exists=True)
            )


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    """Start FastAPI application.

    Returns:
    -------
        FastAPI: FastAPI application as TestClient
    """
    app = FastAPI()

    app.include_router(healthcheck.router)
    app.include_router(tag.router)

    with TestClient(app) as client:
        yield client
