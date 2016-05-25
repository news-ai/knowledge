# Stdlib imports
import time
import json

# Third-party app imports
import requests

# Imports from app
from middleware import config
from knowledge.internal.context import get_login_token, get_types
from knowledge.entity_extraction import entity_extract
from taskrunner import app

base_url = config.BASE_URL


@app.task
def process_single_article(article_id, types):
    token = get_login_token()
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    r = requests.get(
        base_url + '/articles/' + article_id + '/', headers=headers, verify=False)
    article = r.json()
    res = celery_app.send_task(
        'knowledge.entity_extraction.entity_extract', ([article, types, token]))
    return True
