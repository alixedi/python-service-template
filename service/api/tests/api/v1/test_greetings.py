import json


def test_get(client):

    response = client.get(
        '/v1/greetings/1'
    )
    assert response.status_code == 200

    data = response.get_json()
    assert data == {'message': 'Hello World!'}


def test_post(client):

    greeting = {
        'name': 'John',
        'hello': 'Hola'
    }

    response = client.post(
        '/v1/greetings/',
        headers={
            'Content-type': 'Application/json'
        },
        data=json.dumps(greeting)
    )
    assert response.status_code == 200

    data = response.get_json()
    assert data == greeting