from flask import Blueprint, request, jsonify, current_app as app

# TODO: I want to strongly discourage
# direct use of db in views. This will go
# as soon as DAL appears.
from service.db.models.greetings import User


bp = Blueprint(__name__, __name__)


@bp.route("/<user_id>", methods=('get',))
def get(user_id):
    user = User.get_user(app.db_session, user_id)
    greeting = getattr(user, 'greeting', 'Hello World!')
    return jsonify(
        {'message': greeting}
    )


@bp.route("/", methods=('post',))
def post():
    data = request.get_json()
    user = User(**data)
    app.db_session.add(user)
    app.db_session.commit()
    return jsonify(
        {
            'name': 'John',
            'hello': 'Hola'
        }
    )