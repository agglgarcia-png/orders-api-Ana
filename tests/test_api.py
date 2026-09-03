from fastapi.testclient import TestClient

from orders_api.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Orders API running"
    }