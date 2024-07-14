"""Healthcheck route module."""

import logging

from fastapi import APIRouter, status
from service.schemas.healthcheck import HealthCheckModel

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
    responses={400: {"description": "Server error"}},
)


@router.get(
    "/",
    response_model=HealthCheckModel,
    response_description="Simple Healthcheck",
    status_code=status.HTTP_200_OK,
)
async def healthcheck() -> HealthCheckModel:
    """Healthcheck endpoint.

    Simple endpoint to check if the app is running.
    Can be used for a liveness probe in Kubernetes.

    Returns:
        HealthCheckModel: Response with status ok
    """
    return {"status": "ok"}
