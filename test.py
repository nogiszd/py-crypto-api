from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello":"world"}
    
def test_read_main_fetch():
    response = client.get("/v1/1+btc+to+usd")
    assert response.status_code == 200
    
def test_read_main_empty_query():
    response = client.get("/v1/empty")
    assert response.status_code == 400
    assert response.json() == {"detail": "empty query is empty"}