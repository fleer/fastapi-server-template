"""Config schema for service."""

from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    """DatabaseConfig schema class.

    Simple class to define the database configuration.
    """

    host: str
    db_name: str
    port: int
    user: str
    password: str


class Config(BaseModel):
    """Config schema class.

    Full configuration schema for service.
    It mainly contains the version and connection details.

    """

    database: DatabaseConfig
