"""Service API Gateway."""

import logging

import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

import service
from service.prometheus_metrics import cpu_usage, ram_usage
from service.routes.v1 import router
from service.utils import get_config

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

app.router.include_router(router)

# Start Prometheus instrumentator
Instrumentator().instrument(app).add(ram_usage()).add(cpu_usage()).expose(app)


def start() -> None:
    """Launched with `poetry run start` at root level."""
    uvicorn.run("service.api:app", host="0.0.0.0", port=8000)
