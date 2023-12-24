from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import backend

client = TestClient(backend)


def test_predict_endpoint():
    response = client.post("/predict")

    assert response.status_code == 200

    expected_response = {
        "breed1": "Scottish",
        "breed2": "Persian",
    }
    assert response.json() == expected_response

    assert "breed1" in response.json()
    assert isinstance(response.json()["breed1"], str) and response.json()["breed1"]

    assert set(response.json().keys()) == {"breed1", "breed2"}
