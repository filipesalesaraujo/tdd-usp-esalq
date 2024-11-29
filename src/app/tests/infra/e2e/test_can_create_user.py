from fastapi.testclient import TestClient
from uuid import UUID
from infra.api.main import app

client = TestClient(app)

# TESTAR SE E POSSIVEL CRIAR UM USUARIO ATRAVES DA API

def test_can_create_user():
    response = client.post("/users/", json={"name": "Test User"})
    data = response.json()
    assert response.status_code == 200
    assert isinstance(UUID(data["id"]), UUID)
    assert data["name"] == "Test User"
