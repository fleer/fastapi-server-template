"""Utility functions for prediction."""

import logging
import sys
from pathlib import Path

import yaml
from pydantic import ValidationError
from yaml.loader import SafeLoader

from service.config import CONFIG_DIR
from service.schemas.config import Config

logger = logging.getLogger(__name__)


def load_config(config_dir: str = CONFIG_DIR) -> Config:
    """Load configuration file.

    Args:
        config_path: path to configuration file

    Returns:
    -------
        Dictionary with config
    """
    config_path = Path.joinpath(Path(config_dir), "config.yaml")
    try:
        # Open the file and load the file
        with config_path.open() as f:
            return yaml.load(f, Loader=SafeLoader)
    except yaml.YAMLError as exc:
        logger.error(exc)
        logger.error("Could not load %s!", config_path)
        sys.exit(1)


def get_config() -> Config:
    """Get configuration."""
    try:
        return Config.model_validate(load_config())
    except ValidationError as e:
        logger.error("Error in configuration file: %s", e)
        sys.exit(1)
