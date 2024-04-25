import os
import json
import pytest
from fastapi.testclient import TestClient
from api.llm.index import app

client = TestClient(app)

def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Pong!"}

def test_generate_text_valid_input():
    data = {
        "prompt": "Once upon a time, there was a",
        "model": "claude-3-haiku",
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = client.post("/generate_text", json=data)
    assert response.status_code == 200
    assert "result" in response.json()

def test_generate_text_missing_required_field():
    data = {
        "prompt": "Once upon a time, there was a",
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = client.post("/generate_text", json=data)
    assert response.status_code == 400
    assert "field required" in response.json()["detail"]

def test_generate_text_invalid_field_type():
    data = {
        "prompt": "Once upon a time, there was a",
        "model": "claude-3-haiku",
        "temperature": "0.7",
        "max_tokens": 50,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = client.post("/generate_text", json=data)
    assert response.status_code == 422
    assert "value is not a valid float" in response.json()["detail"][0]["msg"]

def test_generate_text_invalid_model():
    data = {
        "prompt": "Once upon a time, there was a",
        "model": "invalid-model",
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = client.post("/generate_text", json=data)
    assert response.status_code == 400
    assert "Invalid model" in response.json()["detail"]

def test_generate_text_openai_error():
    data = {
        "prompt": "Once upon a time, there was a",
        "model": "claude-3-haiku",
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    with pytest.raises(Exception):
        response = client.post("/generate_text", json=data)
        response.raise_for_status()

if __name__ == "__main__":
    pytest.main()