from flask import Flask

from service import db

# TODO: Magically import all the blueprints ffs
from service.api.v1 import greetings

from service.api.config import Config

# TODO: How to pass config?
# TODO: Howw to register cli commands?
def create_app(config=None):
    app = Flask(__name__)
    app.register_blueprint(greetings.bp, url_prefix='/v1/greetings')

    # We shound't have to create engine
    engine = db.create_engine(Config.dsn)
    app.db_session = db.create_session(engine)

    # TODO this is fugly. Can we work around this by
    # subclassinf Flask instead?
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.db_session.remove()

    return app
