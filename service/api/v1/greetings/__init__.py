# We must import all the views here because Flask 
# has no other way to load the modules

from flask import Blueprint, request, jsonify

bp = Blueprint(__name__, __name__)

@bp.route("/", methods=('get',))
def get():
    if user.auth:
        return jsonify(
            {'message': f'Hello { user.name }!'}
        )
    else:
        return jsonify(
            {'message': 'Hello there!'}
        )


@bp.route("/", methods=('post',))
def post():
    data = request.get_json()
    if 'greeting' in data:
        user.greeting = data['greeting']