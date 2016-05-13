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
    response = entity_extract(article, types, token)
    return response


@app.task
def process_all_articles(types, token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    # API sometimes caches values so we can go ahead and add a small
    # token to remove that cache
    small_token = str(int(time.time() * 1000))

    # To sort by date do: ordering=-added_at
    r = requests.get(
        base_url + '/articles/?' + small_token + '&entities_processed=False&ordering=-added_at', headers=headers, verify=False)
    articles = r.json()['results']
    # for article in articles:
    article = articles[0]
    response = None
    if len(article['entity_scores']) is 0:
        response = entity_extract(article, types, token)
    return response
