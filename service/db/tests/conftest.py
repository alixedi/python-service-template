import pytest
from sqlalchemy import orm, exc

from service.db import Config
from service.db import create_engine, create_session


engine = create_engine(Config.dsn)


@pytest.fixture(scope='function')
def session():
    conn = engine.connect()
    transaction = conn.begin()
    session = create_session(conn)
    yield session
    # No need to retain the junk we
    # put in the DB for testing.
    transaction.rollback()
    conn.close()
    session.remove()
