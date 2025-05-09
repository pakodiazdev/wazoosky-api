import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_example_register_payload():
    client = APIClient()
    response = client.get("/api/auth/registre/example")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    # Validate keys in response
    assert "username" in data
    assert "email" in data
    assert "password" in data

    # Validate types
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)
    assert isinstance(data["password"], str)
