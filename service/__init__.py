"""Main module."""

import logging
import logging.config
import os
from datetime import datetime
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from .config import CONFIG_DIR, LOG_DIR


def setup_logging() -> None:
    """Load logging configuration."""
    config = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}.get(
        os.getenv("STAGE", "dev"), "logging.dev.ini"
    )
    config_path = Path.joinpath(Path(CONFIG_DIR), config)

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
