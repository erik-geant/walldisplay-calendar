import json

import jsonschema

CONFIG_SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'str-param': {'type': 'string'},
        'int-param': {'type': 'integer'}
    },
    'required': ['str-param', 'int-param'],
    'additionalProperties': False
}


def load(f):
    """
    loads, validates and returns configuration parameters

    :param f: file-like object that produces the config file
    :return:
    """
    config = json.loads(f.read())
    jsonschema.validate(config, CONFIG_SCHEMA)
    return config
