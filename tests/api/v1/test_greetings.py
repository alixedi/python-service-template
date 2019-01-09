import json

def test_get(client):

    response = client.get(
        '/v1/greeting/'
    )

    data = json.loads(
        response.get_data()
    )

    assert response.status_code == 200
    assert data == {'message': 'Hello World!'}


def test_get_auth(client, test_user):

    response = client.get(
        '/v1/greeting',
        headers=test_user.header
    )

    data = json.loads(
        response.get_data()
    )

    assert response.status_code == 200
    assert data == {'message': f'Hello { test_user.name }!'}


def test_get_post(client, test_user, test_greeting):

    response = client.post(
        '/v1/greeting',
        headers=test_user.header,
        data=test_greeting
    )

    data = json.loads(
        response.get_data()
    )

    assert response.status_code == 200
    assert data == {
        'message': f'Greeting updated',
        'value': test_greeting
    }