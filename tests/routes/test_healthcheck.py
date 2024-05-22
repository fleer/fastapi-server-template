"""Test healthcheck endpoint."""

from fastapi import status
from fastapi.testclient import TestClient


def test_healthcheck(client: TestClient) -> None:
    """Test healthcheck endpoint.

    Arguments:
    ----------
    client {TestClient} -- FastAPI TestClient
    """
    response = client.get("/healthcheck")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
