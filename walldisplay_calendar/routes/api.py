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
from dateutil.parser import isoparse

from flask import Blueprint, jsonify
from walldisplay_calendar.routes import common

routes = Blueprint("walldisplay-calendar-api", __name__)
EMS_LONG_EVENT_THRESHOLD_S = 7 * 24 * 60 * 60  # 7 days
EMS_EVENT_QUERY_WINDOW = '32d'
EMS_EXPORT_URI = ('https://events.geant.org/export/categ/0.json'
                  f'?from=-{EMS_EVENT_QUERY_WINDOW}'
                  f'&to={EMS_EVENT_QUERY_WINDOW}')

EVENT_LIST_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',

    'definitions': {
        'timezone': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'url': {'type': 'string'},
                'title': {'type': 'string'},
                'endDate': {'type': 'string'},
                'startDate': {'type': 'string'},
                'timezone': {'type': 'string'}
            },
            'required': [
                'id', 'url', 'title', 'endDate', 'startDate', 'timezone'],
            'additionalProperties': False
        }
    },

    'type': 'array',
    'items': {'$ref': '#/definitions/timezone'}
}


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
        walldisplay_calendar.routes.api.EVENT_LIST_SCHEMA

    :return:
    """
    r = requests.get(EMS_EXPORT_URI, headers={'Accept': 'application/json'})
    r.raise_for_status()
    response = r.json()

    def _format_date(dd):
        d = date_parser(f'{dd["date"]} {dd["time"]} {dd["tz"]}')
        return d.isoformat()

    def _make_event(e):
        return {
            'id': int(e['id']),
            'url': e['url'],
            'title': e['title'],
            'endDate': _format_date(e['endDate']),
            'startDate': _format_date(e['startDate']),
            'timezone': e['timezone'],
        }

    def _not_too_long(e):
        end = isoparse(e['endDate'])
        start = isoparse(e['startDate'])
        duration_s = (end - start).total_seconds()
        return duration_s <= EMS_LONG_EVENT_THRESHOLD_S

    events = map(_make_event, response['results'])
    short_events = filter(_not_too_long, events)
    return jsonify(list(short_events))
