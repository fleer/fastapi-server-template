"""Healthcheck route module."""

import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from service.database import models
from service.schemas.tag import TagBaseModel, TagModel

from . import get_db

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/tag",
    tags=["Tags"],
    responses={400: {"description": "Server error"}},
)


@router.post(
    "/",
    response_model=TagModel,
    response_description="Create a new tag",
    status_code=status.HTTP_201_CREATED,
)
async def create_tag(request: TagBaseModel, db: Session = Depends(get_db)) -> TagModel:
    """Create a new tag.

    Function for create a new tag in database.

    Args:
        request (TagBaseModel): Request
        db (Session): Database session

    Returns:
        TagModel: Response with new Tag
    """
    db_tag = models.Test(
        tag=request.tag,
    )
    logging.debug("New tag: %s", db_tag)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
