"""
Utilities used by multiple route blueprints.
"""
import functools
import logging
from flask import request, Response

logger = logging.getLogger(__name__)
_DECODE_TYPE_XML = 'xml'
_DECODE_TYPE_JSON = 'json'


def require_accepts_json(f):
    """
    used as a route handler decorator to return an error
    unless the request allows responses with type "application/json"
    :param f: the function to be decorated
    :return: the decorated function
    """
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        # TODO: use best_match to disallow */* ...?
        if not request.accept_mimetypes.accept_json:
            return Response(
                response="response will be json",
                status=406,
                mimetype="text/html")
        return f(*args, **kwargs)
    return decorated_function


def after_request(response):
    """
    Generic function to do additional logging of requests & responses.

    :param response:
    :return:
    """
    if response.status_code != 200:

        try:
            data = response.data.decode('utf-8')
        except Exception:
            # never expected to happen, but we don't want any failures here
            logging.exception('INTERNAL DECODING ERROR')
            data = 'decoding error (see logs)'

        logger.warning('"%s %s" "%s" %s' % (
            request.method,
            request.path,
            data,
            str(response.status_code)))
    return response
