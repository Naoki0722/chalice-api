import json
from chalice.test import Client
from app import app


def test_ルートが通るか():
    with Client(app) as client:
        response = client.http.get("/")
        assert response.json_body == {"hello": "world"}


def test_helloルートが通るか():
    with Client(app) as client:
        response = client.http.get("/hello/test")
        assert response.json_body == {"hello": "test"}


def test_登録できるか():
    with Client(app) as client:
        response = client.http.post(
            "/users",
            headers={"Content-Type": "application/json"},
            body=json.dumps({"example": "json"}),
        )
        assert response.json_body == {"user": {"example": "json"}}


def test_POST以外はエラーとなる():
    with Client(app) as client:
        response = client.http.put(
            "/users",
            headers={"Content-Type": "application/json"},
            body=json.dumps({"example": "json"}),
        )
        assert response.json_body == {
            "Code": "MethodNotAllowedError",
            "Message": "Unsupported method: PUT",
        }


def test_GETはエラーとなる():
    with Client(app) as client:
        response = client.http.get("/users")
        assert response.json_body == {
            "Code": "MethodNotAllowedError",
            "Message": "Unsupported method: GET",
        }


def test_例外処理():
    with Client(app) as client:
        response = client.http.get("/badrequest")
        assert response.json_body == {
            "Code": "BadRequestError",
            "Message": "This is a bad request",
        }
