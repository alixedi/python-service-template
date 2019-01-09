import sqlalchemy as sqla import create_engine as sqla_create_engine
import sqlalchemy.orm as orm import scoped_session, sessionmaker

from models import Base

def create_engine():
    return sqla.create_engine('sqlite:////tmp/test.db', convert_unicode=True)

def init_db(engine):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models.greetings
    Base.metadata.create_all(bind=engine)


def create_session(engine):
    """ Create a session for accessing the DB.
    """
    return scoped_session(
        sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )

def register(app):
    app.db = 