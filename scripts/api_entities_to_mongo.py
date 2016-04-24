# Stdlib imports
import json
import time

# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pymongo import MongoClient

# Imports from app
from middleware import config

# MongoDB setup
client = MongoClient(connect=False)
db = client.knowledge
entity_collection = db.entities

base_url = 'https://context.newsai.org/api'


def get_entity_by_id(entity, token):
    mongo_entity = entity_collection.find_one({'name': entity['name']})
    if mongo_entity:
        print 'mongo'
        return mongo_entity
    mongo_entity = entity_collection.insert_one(entity)
    print 'adding'
    return mongo_entity


def get_all_entities(token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    small_token = str(int(time.time() * 1000))
    limit = 80984

    for amount in range(1, limit):
        r = requests.get(base_url + "/entities/" + str(amount) +
                         "?" + small_token, headers=headers, verify=False)
        r = r.json()
        print get_entity_by_id(r, token)
