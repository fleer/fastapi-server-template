"""Tag Repository.

Abstracts the data access layer
by offering a clean interface for interacting
with the underlying data storage.
"""

import logging
from typing import List, Optional, Type

from service.database.models import Tag
from service.schemas.tag_schema import TagInput, TagOutput
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class TagRepository:
    """A repository for handling operations related to the Tag model."""

    def __init__(self, session: Session) -> None:
        """Initializes the repository with a database session.

        Args:
            session (Session): The database session to use for queries.
        """
        self.session = session

    def create(self, data: TagInput) -> TagOutput:
        """Creates a new tag record in the database.

        Args:
            data (TagInput): The input data for the new tag.

        Returns:
            TagOutput: The created tag output.
        """
        tag = Tag(**data.model_dump(exclude_none=True))
        logging.debug("New tag: %s", tag)
        self.session.add(tag)
        self.session.commit()
        self.session.refresh(tag)
        return TagOutput(
            id=tag.id,
            timestamp=tag.timestamp,
            tag=tag.tag,
        )

    def get_all(self) -> List[Optional[TagOutput]]:
        """Retrieves all tag records from the database.

        Returns:
            List[Optional[TagOutput]]: A list of all tag outputs.
        """
        tags = self.session.query(Tag).all()
        return [TagOutput(**tag.__dict__) for tag in tags]

    def get_by_id(self, _id: int) -> Type[Tag]:
        """Retrieves a tag record by its ID.

        Args:
            _id (int): The ID of the tag to retrieve.

        Returns:
            Type[Tag]: The tag with the given ID.
        """
        return self.session.query(Tag).filter_by(id=_id).first()

    def tag_exists_by_id(self, _id: int) -> bool:
        """Checks if a tag exists by its ID.

        Args:
            _id (int): The ID of the tag to check.

        Returns:
            bool: True if the tag exists, False otherwise.
        """
        tag = self.session.query(Tag).filter_by(id=_id).first()
        return tag is not None

    def update(self, tag: Type[Tag], data: TagInput) -> TagInput:
        """Updates a tag record in the database.

        Args:
            tag (Type[Tag]): The tag to update.
            data (TagInput): The new data for the tag.

        Returns:
            TagInput: The updated tag input.
        """
        tag.tag = data.tag
        self.session.commit()
        self.session.refresh(tag)
        return TagInput(**tag.__dict__)

    def delete(self, tag: Type[Tag]) -> bool:
        """Deletes a tag record from the database.

        Args:
            tag (Type[Tag]): The tag to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        self.session.delete(tag)
        self.session.commit()
        return True
