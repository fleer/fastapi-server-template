"""Health check schema."""

from pydantic import BaseModel


class HealthCheckModel(BaseModel):
    """Class with health check information.

    Simple response for life check of the service.

    Attributes
    ----------
    status: str
        The status of the service
    """

    status: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "status": "ok",
            },
        }
    }
