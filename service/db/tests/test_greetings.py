import pytest

from service.db.models.greetings import User

@pytest.mark.parametrize(
    'hello, name, greeting', [
        (None, None, 'Hello World!'),
        ('Hello', 'Micky', 'Hello Micky!'),
        ('こんにちは', 'ミッキー', 'こんにちは ミッキー!')
    ]
)
def test_greetings(session, hello, name, greeting):
    user = User(hello=hello, name=name)
    session.add(user)
    session.commit()
    users = session.query(User).all()
    assert len(users) == 1

    user = session.query(User).one()
    assert str(users[0]) == greeting
