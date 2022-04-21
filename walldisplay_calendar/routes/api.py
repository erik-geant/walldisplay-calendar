"""
API Endpoints
=========================

.. contents:: :local:

/api/events
---------------------

.. autofunction:: walldisplay_calendar.routes.api.events

"""
import requests
from dateutil.parser import parse as date_parser

from flask import Blueprint, jsonify
from walldisplay_calendar.routes import common

routes = Blueprint("walldisplay-calendar-api", __name__)

EMS_EXPORT_URI = 'https://events.geant.org/export/categ/0.json?from=-32d&to=32d'

# EVENT_LIST_SCHEMA = {
#     '$schema': 'http://json-schema.org/draft-07/schema#',
#
#     'definitions': {
#         'thing': {
#             'type': 'object',
#             'properties': {
#                 'id': {'type': 'string'},
#                 'time': {'type': 'number'},
#                 'state': {'type': 'boolean'},
#                 'data1': {'type': 'string'},
#                 'data2': {'type': 'string'},
#                 'data3': {'type': 'string'}
#             },
#             'required': ['id', 'time', 'state', 'data1', 'data2', 'data3'],
#             'additionalProperties': False
#         }
#     },
#
#     'type': 'array',
#     'items': {'$ref': '#/definitions/thing'}
# }


@routes.after_request
def after_request(resp):
    return common.after_request(resp)


@routes.route("/events", methods=['GET', 'POST'])
@common.require_accepts_json
def load_events():
    """
    handler for /api/events requests

    response will be formatted as:

    .. asjson::
        walldisplay_calendar.routes.api.THING_LIST_SCHEMA

    :return:
    """
    r = requests.get(EMS_EXPORT_URI, headers={'Accept': 'application/json'})
    r.raise_for_status()
    response = r.json()

    def _make_date(dd):
        d = date_parser(f'{dd["date"]} {dd["time"]} {dd["tz"]}')
        return d.isoformat()

    def _make_event(e):
        return {
            'id': int(e['id']),
            'url': e['url'],
            'title': e['title'],
            'endDate': _make_date(e['endDate']),
            'startDate': _make_date(e['startDate']),
            'timezone': e['timezone'],
        }

    return jsonify(list(map(_make_event, response['results'])))
