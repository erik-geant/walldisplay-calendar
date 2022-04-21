.. api intro

API Protocol
===============

This module implements a Flask-based webservice which
communicates with clients over HTTP.
Responses to valid requests are returned as JSON messages.
The server will therefore return an error unless
`application/json` is in the `Accept` request header field.

HTTP communication and JSON grammar details are
beyond the scope of this document.
Please refer to [RFC 2616](https://tools.ietf.org/html/rfc2616)
and www.json.org for more details.

.. contents:: :local:

.. automodule:: walldisplay_calendar.routes.default

.. automodule:: walldisplay_calendar.routes.api

