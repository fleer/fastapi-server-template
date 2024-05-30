"""Configuration for pytest."""

import os
from shutil import copytree
from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import Connection, create_engine
from sqlalchemy.orm import Session, sessionmaker

import alembic.config
from service.config import CONFIG_DIR
from service.database import database, models
from service.routes import get_db, healthcheck

connection_string, schema = database.get_db_config(CONFIG_DIR, "test")
engine = create_engine(connection_string)

SessionTesting = sessionmaker(bind=engine)

ALEMBIC_CONFIG = "alembic.ini"


def migrate_in_memory(
    migrations_path: str,
    alembic_ini_path: str = ALEMBIC_CONFIG,
    connection: Connection = None,
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
    if connection is not None:
        config.attributes["connection"] = connection
    alembic.command.upgrade(config, revision)


def start_application() -> FastAPI:
    """Start FastAPI application.

    Returns:
    -------
        FastAPI: FastAPI application
    """
    app = FastAPI()

    app.include_router(healthcheck.router)
    return app


def pytest_sessionstart() -> None:
    """Set up the database."""
    os.environ["STAGE"] = "test"
    db_engine = create_engine(connection_string)
    database.create_database_with_schema_if_not_exists(
        db_engine, schema, reset_schema=True
    )
    db_engine.dispose()


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


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """Create a fresh database on each test case.

    Use alembic if the config file exists,
    otherwise create the tables directly.

    """
    db_engine = create_engine(connection_string)
    with db_engine.begin() as connection:
        migrate_in_memory("alembic", ALEMBIC_CONFIG, connection)
    _app = start_application()
    yield _app
    models.Base.metadata.drop_all(bind=db_engine)
    db_engine.dispose()


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[Session, Any, None]:
    """Create a database connection for testing."""
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """TestClient.

    API TestClient that uses the `db_session`
    fixture to override the `get_db` dependency
    that is injected into routes.
    """

    def _get_test_db() -> Generator[SessionTesting, Any, None]:
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
