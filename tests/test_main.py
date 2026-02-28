from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    response = client.get("/add/2/3")
    assert response.json()["result"] == 5
