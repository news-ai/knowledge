# Stdlib imports
import time
import os
import json

# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Imports from app
from middleware import config

# Removing requests warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
