from flask import Flask, request, make_response
from flask_cors import CORS

from api.api import api
from api.config import Config


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    api.init_app(app)


app = create_app(Config)


if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
