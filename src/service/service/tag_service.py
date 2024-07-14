"""Tag service layer."""

from typing import List, Optional

from fastapi import HTTPException
from service.repository.tag_repository import TagRepository
from service.schemas.tag_schema import TagInput, TagOutput
from sqlalchemy.orm import Session


class TagService:
    """Service class for handling operations related to Tags."""

    def __init__(self, session: Session) -> None:
        """Initialize the TagService with a database session.

        Args:
            session (Session): The database session to use for repository operations.
        """
        self.repository = TagRepository(session)

    def create(self, data: TagInput) -> TagOutput:
        """Create a new Tag.

        Args:
            data (TagInput): The input data for the new Tag.

        Returns:
            TagOutput: The created Tag.
        """
        return self.repository.create(data)

    def get_all(self) -> List[Optional[TagOutput]]:
        """Get all Tags.

        Returns:
            List[Optional[TagOutput]]: A list of all Tags.
        """
        return self.repository.get_all()

    def delete(self, _id: int) -> bool:
        """Delete a Tag.

        Args:
            _id (int): The id of the Tag to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.

        Raises:
            HTTPException: If no Tag with the given id exists.
        """
        if not self.repository.tag_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="Tag not found")
        tag = self.repository.get_by_id(_id)
        self.repository.delete(tag)
        return True

    def update(self, _id: int, data: TagInput) -> TagInput:
        """Update a Tag.

        Args:
            _id (int): The id of the Tag to update.
            data (TagInput): The new data for the Tag.

        Returns:
            TagInput: The updated Tag.

        Raises:
            HTTPException: If no Tag with the given id exists.
        """
        if not self.repository.tag_exists_by_id(_id):
            raise HTTPException(status_code=404, detail="Tag not found")
        tag = self.repository.get_by_id(_id)
        return self.repository.update(tag, data)
