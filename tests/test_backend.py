#!/usr/bin/python3
# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import backend

client = TestClient(backend)


def test_predict_endpoint():
    response = client.post("/predict")

    expected_response = {
        "Scottish Fold": 0.98,
        "Persian": 0.0001,
        "Norwegian Forest": 0.1
    }

    assert response.status_code == 200
    assert response.json() == expected_response
    assert "Scottish Fold" in response.json()
    assert isinstance(response.json()["Scottish Fold"], str) and response.json()["Scottish Fold"]
    assert isinstance(response.json().values(), float)

