from fastapi.testclient import TestClient

from ai_bundle.main import app


def test_root():
    """Test of main function."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
