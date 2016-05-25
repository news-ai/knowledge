# Stdlib imports
import json
import logging

# Third-party app imports
from raven.contrib.flask import Sentry
from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from flask_restful import Resource, Api, reqparse

# Imports from app
from middleware.config import (
    SENTRY_USER,
    SENTRY_PASSWORD,
    SENTRY_APP_ID,
)
from knowledge.internal.context import get_login_token, get_types
from knowledge.articles import process_single_article

# Setting up Flask and API
app = Flask(__name__)
api = Api(app)
CORS(app)

# Setting up Sentry
sentry = Sentry(
    app, dsn='https://' + SENTRY_USER + ':' + SENTRY_PASSWORD + '@app.getsentry.com/' + SENTRY_APP_ID)
logger = logging.getLogger("sentry.errors")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

types = {}

# Setting up parser
parser = reqparse.RequestParser()
parser.add_argument('id')


# Route to POST data for news processing
class Knowledge(Resource):

    def post(self):
        args = parser.parse_args()
        res = process_single_article.apply_async(
            [args['id'], types])
        return str(res.task_id)

api.add_resource(Knowledge, '/knowledge')

if __name__ == "__main__":
    token = get_login_token()
    types = get_types(token)
    app.run(port=int('8000'), debug=False)
