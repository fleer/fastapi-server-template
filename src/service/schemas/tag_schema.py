"""Health check schema."""

from datetime import datetime

from service.schemas.camel_case import CamelModel


class TagInput(CamelModel):
    """Class with tag information.

    Simple response Model for creating and
    reading tags.

    Attributes:
    ----------
    tag: str
        Given tag
    """

    tag: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "tag": "test",
            },
        }
    }


class TagOutput(CamelModel):
    """Class with tag information.

    Simple response Model for creating and
    reading tags.

    Attributes:
    ----------
    tag: str
        Given tag
    """

    id: int
    timestamp: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "tag": "test",
                "timestamp": "2021-01-01T00:00:00",
            },
        }
    }
