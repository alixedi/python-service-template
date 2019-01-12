import pytest

from service.api import create_app, Config
from service.db import create_engine, create_session


engine = create_engine(Config.dsn)


@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    This is a client fixture but it
    also sets up the transactional
    session so that we don't pollute
    the DB in tests.
    """
    conn = engine.connect()
    transaction = conn.begin()
    app.db_session = create_session(conn)
    yield app.test_client()
    # No need to retain the junk we
    # put in the DB for testing.
    transaction.rollback()
    conn.close()
    app.db_session.remove()

