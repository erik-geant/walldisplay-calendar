import json
import jsonschema
import pytest

from walldisplay_calendar.routes.default import VERSION_SCHEMA
from walldisplay_calendar.routes.api import THING_LIST_SCHEMA


@pytest.mark.parametrize(
    'endpoint',
    ['version', 'api/things'])
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


def test_things(client):

    rv = client.post(
        'api/things',
        headers={'Accept': ['application/json']})
    assert rv.status_code == 200
    result = json.loads(rv.data.decode('utf-8'))
    jsonschema.validate(result, THING_LIST_SCHEMA)
