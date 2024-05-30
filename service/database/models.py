"""Database Models.

Module with database definitions.
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
    """Test class.

    Class for test table.
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
