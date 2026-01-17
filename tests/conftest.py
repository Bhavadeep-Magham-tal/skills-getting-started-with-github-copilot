import pytest
from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture
def client():
    """FastAPI test client fixture"""
    return TestClient(app)