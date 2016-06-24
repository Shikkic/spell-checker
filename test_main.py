import pytest
import main

@pytest.fixture
def app():
  return main.app

@pytest.fixture
def test_client(app):
  return app.test_client()

def test_title(test_client):
  response = test_client.get("/")
  assert "Check Yo Self" in response.data.decode("utf-8")

def test_text_box(test_client):
  response = test_client.get("/")
  
