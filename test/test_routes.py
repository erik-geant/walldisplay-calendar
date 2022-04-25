import json
import os
import re

from dateutil.parser import isoparse
import jsonschema
import pytest
import responses

from walldisplay_calendar.routes.default import VERSION_SCHEMA
from walldisplay_calendar.routes.api \
    import EVENT_LIST_SCHEMA, EMS_LONG_EVENT_THRESHOLD_S

@pytest.mark.parametrize(
    'endpoint',
    ['version', 'api/events'])
def test_bad_accept(endpoint, client):
    rv = client.post(
        endpoint,
        headers={'Accept': ['text/html']})
    assert rv.status_code == 406


def test_version_request(client):

    rv = client.post(
        'version',
        headers={'Accept': ['application/json']})
    assert rv.status_code == 200
    result = json.loads(rv.data.decode('utf-8'))
    jsonschema.validate(result, VERSION_SCHEMA)


@responses.activate
def test_events(client):

    test_data_filename = os.path.join(
        os.path.dirname(__file__), 'ems-events-export.json')
    with open(test_data_filename) as f:
        responses.add(
            method=responses.GET,
            url=re.compile(r'.*export/categ/0.json.*'),
            json=json.loads(f.read()))

    rv = client.post(
        'api/events',
        headers={'Accept': ['application/json']})
    assert rv.status_code == 200
    events = json.loads(rv.data.decode('utf-8'))
    jsonschema.validate(events, EVENT_LIST_SCHEMA)
    assert events  # sanity: test data has at least one trap

    def _duration(e):
        start = isoparse(e['startDate'])
        end = isoparse(e['endDate'])
        return (end - start).total_seconds()

    def _short_enough(e):
        return _duration(e) <= EMS_LONG_EVENT_THRESHOLD_S

    assert all(map(_short_enough, events))
