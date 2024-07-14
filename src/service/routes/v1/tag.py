"""Healthcheck route module."""

import logging

from fastapi import APIRouter, Depends, status
from service.routes import get_db
from service.schemas.tag_schema import TagInput, TagOutput
from service.service.tag_service import TagService
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/tag",
    tags=["Tags"],
    responses={400: {"description": "Server error"}},
)


@router.post(
    "",
    response_model=TagOutput,
    response_description="Create a new tag",
    status_code=status.HTTP_201_CREATED,
)
async def create_entry(request: TagInput, db: Session = Depends(get_db)) -> TagOutput:
    """Asynchronously create a new measurement entry.

    Args:
        request (TagInput): The input data for the new Tag.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        TagOutput: The created Tag.
    """
    return TagService(db).create(request)
