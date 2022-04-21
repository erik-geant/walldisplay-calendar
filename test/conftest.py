import json
import os
import tempfile

import pytest

import walldisplay_calendar


@pytest.fixture
def data_config_filename():
    test_config_data = {
        'str-param': 'test data string',
        'int-param': -47
    }
    with tempfile.NamedTemporaryFile() as f:
        f.write(json.dumps(test_config_data).encode('utf-8'))
        f.flush()
        yield f.name


@pytest.fixture
def client(data_config_filename):
    os.environ['SETTINGS_FILENAME'] = data_config_filename
    with walldisplay_calendar.create_app().test_client() as c:
        yield c
