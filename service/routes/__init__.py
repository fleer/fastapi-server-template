"""Routes module."""

from typing import Any, Generator

from sqlalchemy.orm import Session

from ..database.database import SessionLocal


# Dependency
def get_db() -> Generator[Session, Any, None]:
    """Get database connection."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
