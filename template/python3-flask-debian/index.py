# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from flask import Flask, request
from function import handler
from waitress import serve
import os
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': os.getenv('LOG_LEVEL', 'ERROR'),
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# distutils.util.strtobool() can throw an exception


def is_true(val):
    return len(val) > 0 and val.lower() == "true" or val == "1"


@app.before_request
def fix_transfer_encoding():
    """
    Sets the "wsgi.input_terminated" environment flag, thus enabling
    Werkzeug to pass chunked requests as streams.  The gunicorn server
    should set this, but it's not yet been implemented.
    """

    transfer_encoding = request.headers.get("Transfer-Encoding", None)
    if transfer_encoding == u"chunked":
        request.environ["wsgi.input_terminated"] = True


@app.route("/", defaults={"path": ""}, methods=["POST", "GET"])
@app.route("/<path:path>", methods=["POST", "GET"])
def main_route(path):
    raw_body = os.getenv("RAW_BODY", "false")

    as_text = True

    if is_true(raw_body):
        as_text = False

    app.logger.info("Receveid Event: 1")
    # app.logger.info('Start OpenFaas Function')

    ret = handler.handle(request.get_data(as_text=as_text))
    return ret


if __name__ == '__main__':
    # if app.debug:
    #     app.logger.
    serve(app, host='0.0.0.0', port=5000)
