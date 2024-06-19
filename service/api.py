"""Schadenrouting API Gateway."""

import logging

import uvicorn
from fastapi import FastAPI

import service

from .routes import healthcheck, tag
from .utils import get_config

logger = logging.getLogger(__name__)


config = get_config()

version = service.__getattr__("__version__")

description = """
# Service API Gateway.

Here is a small description of the project.
"""

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
    },
    openapi_tags=tags_metadata,
)

app.router.include_router(healthcheck.router)
app.router.include_router(tag.router)


def start() -> None:
    """Launched with `poetry run start` at root level."""
    uvicorn.run("service.api:app", host="0.0.0.0", port=8000)
