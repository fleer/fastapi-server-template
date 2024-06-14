"""Tests for tag routes."""

import json

from fastapi import status
from fastapi.testclient import TestClient


def test_tag(client: TestClient) -> None:
    """Test healthcheck endpoint.

    Args:
    ----------
    client {TestClient} -- FastAPI TestClient
    """
    response = client.post("/tag/", data=json.dumps({"tag": "test"}))
    assert response.status_code == status.HTTP_201_CREATED
