import time
import json
import os

import requests

from middleware import log, config
from knowledge.entity_extraction import entity_extract

logger = log.setup_custom_logger('knowledge')

base_url = config.BASE_URL


def get_login_token():
    headers = {
        "content-type": "application/json",
        "accept": "application/json"
    }
    payload = {
        "username": config.CONTEXT_API_USERNAME,
        "password": config.CONTEXT_API_PASSWORD,
    }
    r = requests.post(base_url + "/jwt-token/",
                      headers=headers, data=json.dumps(payload), verify=False)
    data = json.loads(r.text)
    token = data.get('token')
    return token


def get_types(token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    r = requests.get(base_url + "/types/?limit=5000",
                     headers=headers, verify=False)
    types = r.json()['results']
    typeNametoType = {}
    for i in types:
        typeNametoType[i['name']] = i
    return typeNametoType


if __name__ == '__main__':
    token = get_login_token()
    types = get_types(token)

    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    # To sort by date do: ordering=-added_at
    r = requests.get(
        base_url + '/articles/?entities_processed=False&ordering=-added_at', headers=headers, verify=False)
    articles = r.json()['results']
    # for article in articles:
    article = articles[0]
    if len(article['entity_scores']) is 0:
        response = entity_extract(article, types, token)
        print response
