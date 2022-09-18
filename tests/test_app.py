import json
from chalice.test import Client
from app import app

def test_index():
    with Client(app) as client:
        response = client.http.get('/')
        assert response.json_body == {'hello': 'world'}


def test_post_index():
    with Client(app) as client:
        response = client.http.post(
            '/users',
            headers={'Content-Type':'application/json'},
            body=json.dumps({'example':'json'})
        )
        assert response.json_body == { 'user': {'example': 'json'}}
