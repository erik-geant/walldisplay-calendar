"""
automatically invoked app factory
"""
import logging
import os

from flask import Flask
from flask_cors import CORS  # for debugging

from walldisplay_calendar import environment
from walldisplay_calendar import config


def create_app():
    """
    overrides default settings with those found
    in the file read from env var SETTINGS_FILENAME

    :return: a new flask app instance
    """
    #
    # assert 'SETTINGS_FILENAME' in os.environ
    # with open(os.environ['SETTINGS_FILENAME']) as f:
    #     app_config = config.load(f)

    app = Flask(__name__)
    CORS(app)

    app.secret_key = 'super secret session key'
    # app.config['CONFIG_PARAMS'] = app_config

    from walldisplay_calendar.routes import default
    app.register_blueprint(default.routes, url_prefix='/')

    from walldisplay_calendar.routes import api
    app.register_blueprint(api.routes, url_prefix='/api')

    logging.info('Flask app initialized')

    environment.setup_logging()

    return app
