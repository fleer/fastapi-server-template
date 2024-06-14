"""Schadenrouting API Gateway."""

import logging
from pathlib import Path

from fastapi import FastAPI

import service

from .routes import healthcheck, tag
from .utils import get_config

logger = logging.getLogger(__name__)


config = get_config()

version = service.__getattr__("__version__")

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
app.router.include_router(tag.router)
