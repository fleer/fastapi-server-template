"""Database Tables.

Define the database tables for the ORM.
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    Integer,
    String,
    sql,
)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from service.database.database import metadata

Base = declarative_base(metadata=metadata)


class Test(Base):
    """Definition of the test table.

    Attributes:
        __tablename__ (str): Table name
        id (int): Row ID
        tag (str): Desired tag
        timestamp (datetime): Current timestamp
                                is stored here
    """

    __tablename__ = "test"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    tag: Mapped[str] = mapped_column(String, comment="Tag")
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        onupdate=sql.func.now(),
        server_default=sql.func.now(),
        comment="Creation Date",
    )


Base.registry.configure()
