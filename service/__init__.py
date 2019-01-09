from flask import Flask

import api
import db


def create_app(config=None, db=None):

    app = Flask(__name__)
    