"""Schadenrouting API Gateway."""

import logging
from pathlib import Path

from fastapi import FastAPI

from .routes import healthcheck
from .utils import get_config

logger = logging.getLogger(__name__)


config = get_config()
version = config.get("version", "0.0.0")

# Needed if no Git Tag is available
version = "0.0.1" if version == "" else version

description = Path("README.md").read_text()

tags_metadata = [
    {
        "name": "Healthcheck",
        "description": "Live and readiness probes.",
    },
]

app = FastAPI(
    title="FastAPI API Gateway",
    description=description,
    version=version,
    contact={
        "name": "fleer",
        "url": "https://github.com/fleer/fastapi-server-template",
        "email": "",
    },
    openapi_tags=tags_metadata,
)

app.router.include_router(healthcheck.router)
