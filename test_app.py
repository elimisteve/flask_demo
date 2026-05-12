import pytest

from app import app as flask_app


@pytest.fixture
def client():
    return flask_app.test_client()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Welcome to the homepage"


def test_hello_default(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b"Hello visitor!" in response.data


def test_hello_with_name(client):
    response = client.get('/hello/Steve')
    assert response.status_code == 200
    assert b"Hello Steve!" in response.data


def test_hello_trailing_slash(client):
    response = client.get('/hello/')
    assert response.status_code == 200
    assert b"Hello visitor!" in response.data
