"""
Default Endpoints
=========================

.. contents:: :local:

/version
---------------------

.. autofunction:: walldisplay_calendar.routes.default.version

"""
import pkg_resources

from flask import Blueprint, jsonify
from walldisplay_calendar.routes import common

routes = Blueprint("walldisplay-calendar-default", __name__)
API_VERSION = '0.1'

VERSION_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'type': 'object',
    'properties': {
        'api': {
            'type': 'string',
            'pattern': r'\d+\.\d+'
        },
        'module': {
            'type': 'string',
            'pattern': r'\d+\.\d+'
        }
    },
    'required': ['api', 'module'],
    'additionalProperties': False
}


@routes.after_request
def after_request(resp):
    return common.after_request(resp)


@routes.route("/version", methods=['GET', 'POST'])
@common.require_accepts_json
def version():
    """
    handler for /version requests

    response will be formatted as:

    .. asjson::
        walldisplay_calendar.routes.default.VERSION_SCHEMA

    :return:
    """
    version_params = {
        'api': API_VERSION,
        'module':
            pkg_resources.get_distribution('walldisplay-calendar').version
    }
    return jsonify(version_params)
