import time
import json
import os

import requests

from middleware import log, config
from knowledge.entity_extraction import entity_extract

logger = log.setup_custom_logger('knowledge')

base_url = 'https://context.newsai.org/api'


def get_login_token():
    headers = {
        "content-type": "application/json",
        "accept": "application/json"
    }
    payload = {
        "username": os.environ.get("NEWSAI_CONTEXT_API_USERNAME"),
        "password": os.environ.get("NEWSAI_CONTEXT_API_PASSWORD"),
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

    r = requests.get(base_url + '/articles?entities_processed=False', headers=headers,
                     verify=False)
    articles = r.json()['results']
    entity_extract(articles[2], types, token)
