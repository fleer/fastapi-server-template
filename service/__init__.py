"""Main module."""

import importlib.metadata
import logging
import logging.config
import os
from datetime import datetime
from pathlib import Path

import toml
from dotenv import find_dotenv, load_dotenv

from .config import LOG_CONFIG_DIR, LOG_DIR


def __get_package_version() -> str:
    """Find the version of this package."""
    package_version = "unknown"
    try:
        # Try to get the version of the current package if
        # it is running from a distribution.
        package_version = importlib.metadata.version("schadenrouting")
    except importlib.metadata.PackageNotFoundError:
        # Fall back on getting it from a local pyproject.toml.
        # This works in a development environment where the
        # package has not been installed from a distribution.

        pyproject_toml_file = Path(__file__).parent.parent / "pyproject.toml"
        if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
            package_version = toml.load(pyproject_toml_file)["tool"]["poetry"][
                "version"
            ]
            # Indicate it might be locally modified or unreleased.
            package_version = package_version + "-dev"

    return package_version


def __getattr__(name: str) -> str | int:
    """Get package attributes."""
    if name in ("version", "__version__"):
        return __get_package_version()
    else:
        raise AttributeError(f"No attribute {name} in module {__name__}.")


def setup_logging() -> None:
    """Load logging configuration."""
    config = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}.get(
        os.getenv("STAGE", "dev"), "logging.dev.ini"
    )
    config_path = Path.joinpath(Path(LOG_CONFIG_DIR), config)

    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    if not Path(LOG_DIR).exists():
        Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )


# find .env file in parent directory
env_file = find_dotenv()
# Load the users .env file into environment variables
load_dotenv(env_file, verbose=True, override=True)

del load_dotenv
del env_file

setup_logging()
