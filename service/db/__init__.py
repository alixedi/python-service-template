import sqlalchemy as sqla

from service.db.config import Config
from service.db.models import Base

# TODO: We should dynamically import models here
from service.db.models.greetings import User


# TODO: Namespace this in DB class?

def create_engine(dsn):
    """
    Engine in SQLA term is the "home base". I hate the term
    but IMO its better to stick to SQLA vocabulary for this
    than coming up with something better that will not be
    searchable on Google.
    """
    engine = sqla.create_engine(dsn, convert_unicode=True)

    try:
        connection = engine.connect()

    except sqla.exc.OperationalError as e:
        exit(
            (
                f'Cannot connect to Postgres. Please confirm that a Postgres '
                f'instance is accessible at: { dsn }\n'
                f'If you are testing this on your local machine, and you have '
                f'Docker installed and running, you can use `make db` to create '
                f'a new Postgres instance.'
            )
        )

    else:
        connection.close()

    return engine


def create_session(engine):
    """ Create a session for accessing the DB.
    """
    return sqla.orm.scoped_session(
        sqla.orm.sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    )
