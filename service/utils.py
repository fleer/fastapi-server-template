"""Utility functions for prediction."""

import logging
import os
from pathlib import Path

import yaml
from yaml.loader import SafeLoader

from .config import CONFIG_DIR

logger = logging.getLogger(__name__)


def get_config(config_dir: str = CONFIG_DIR) -> dict:
    """Load configuration file.

    Args:
        config_path: path to configuration file

    Returns:
    -------
        Dictionary with config
    """
    config = {"dev": "config.dev.yaml", "prod": "config.yaml"}.get(
        os.getenv("STAGE", "dev"), "config.yaml"
    )
    config_path = Path.joinpath(Path(config_dir), config)
    try:
        # Open the file and load the file
        with open(config_path) as f:
            return yaml.load(f, Loader=SafeLoader)
    except yaml.YAMLError as exc:
        logger.error(exc)
        logger.error("Could not load %s!", config_path)
        return {}
