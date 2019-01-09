import pytest

from service import create_app


@pytest.fixture(scope='session')
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    ctx = app.app_context
    ctx.push()
    yield client
    ctx.pop()


@pytest.fixture(scope='session')
def db(app):
    # TODO: create test databases
    from db import init_db
    db = init_db()
    yield 
    db.drop_all()

@pytest.fixture(scope='function')
def session(db):
    from db import get_db_session
    session = get_db_session()
    
    request.addfinalizer(teardown)
    return session