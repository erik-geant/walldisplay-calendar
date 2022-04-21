# Skeleton Web App

## Overview

This module implements a skeleton Flask-based webservice
and in-browser React front-end.

The webservice communicates with the front end over HTTP.
Responses to valid requests are returned as JSON messages.
The server will therefore return an error unless
`application/json` is in the `Accept` request header field.

HTTP communication and JSON grammar details are
beyond the scope of this document.
Please refer to [RFC 2616](https://tools.ietf.org/html/rfc2616)
and www.json.org for more details.


## Configuration

This app allows specification of a few
example configuration parameters.  These
parameters should stored in a file formatted
similarly to `config.json.example`, and the name
of this file should be stored in the environment
variable `SETTINGS_FILENAME` when running the service.

## Building the web application

The initial repository doesn't contain the required web application.
For instructions on building this see `webapp/README.md`.

## Running this module

This module has been tested in the following execution environments:

- As an embedded Flask application.
For example, the application could be launched as follows:

```bash
$ export FLASK_APP=walldisplay_calendar.app
$ export SETTINGS_FILENAME=config-example.json
$ flask run
```

See https://flask.palletsprojects.com/en/2.1.x/deploying/
for best practices about running in production environments.

### resources

Any non-empty responses are JSON formatted messages.

#### /data/version

  * /version

  The response will be an object
  containing the module and protocol versions of the
  running server and will be formatted as follows:

  ```json
  {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "api": {
                "type": "string",
                "pattern": r'\d+\.\d+'
            },
            "module": {
                "type": "string",
                "pattern": r'\d+\.\d+'
            }
        },
        "required": ["api", "module"],
        "additionalProperties": False
    }
  ```

#### /test/test1

The response will be some json data, as an example ...
