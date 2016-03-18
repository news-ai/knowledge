import time
import os
import requests
import json

from middleware import config

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

    small_token = str(int(time.time() * 1000))

    r = requests.get(base_url + "/types/?" + small_token + "&limit=5000",
                     headers=headers, verify=False)
    types = r.json()['results']
    typeNametoType = {}
    for i in types:
        typeNametoType[i['name']] = i
    return typeNametoType
