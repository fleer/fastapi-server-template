"""Endpoints for v1 of the API."""

from fastapi import APIRouter

from service.routes.v1 import healthcheck, tag

router = APIRouter(prefix="/api/v1")
router.include_router(healthcheck.router)
router.include_router(tag.router)
