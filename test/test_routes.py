import json
import os
import re

import jsonschema
import pytest
import responses

from walldisplay_calendar.routes.default import VERSION_SCHEMA
from walldisplay_calendar.routes.api import EVENT_LIST_SCHEMA


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
    result = json.loads(rv.data.decode('utf-8'))
    jsonschema.validate(result, EVENT_LIST_SCHEMA)
