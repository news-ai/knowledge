# Stdlib imports
import time
import json
import urllib

# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pymongo import MongoClient

# Imports from app
from middleware import config
from knowledge.utils import numerical

# Removing requests warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# MongoDB setup
client = MongoClient(connect=False)
db = client.knowledge
entity_collection = db.entities

base_url = config.BASE_URL


def add_type_to_api(type_name, token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    type_name = urllib.unquote_plus(
        type_name.encode('utf-8')).decode('utf-8')

    small_token = str(int(time.time() * 1000))

    r = requests.get(base_url + "/types/?" + small_token + "&name=" + type_name,
                     headers=headers, verify=False)
    types = r.json()

    api_entity = None

    if types['count'] > 0:
        api_entity = types['count'][0]
    else:
        payload = {
            "name": type_name
        }
        r = requests.post(base_url + "/types/",
                          headers=headers, data=json.dumps(payload), verify=False)
        api_entity = r.json()

    return api_entity


def add_entity_to_api(entity, types, token):
    api_entity = None
    context = {}

    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    entity_name = urllib.unquote_plus(
        entity['text'].encode('utf-8')).decode('utf-8')
    mongo_entity = entity_collection.find_one({'name': entity_name})

    if mongo_entity:
        return mongo_entity

    small_token = str(int(time.time() * 1000))
    r = requests.get(base_url + "/entities/?" + small_token +
                     "&name=" + entity_name, headers=headers, verify=False)
    context = r.json()

    if context['count'] > 0:
        api_entity = context['results'][0]
    else:
        types_url = base_url + '/types/'

        typeId = ''
        if entity['type'] in types:
            typeId = str(types[entity['type']]['id'])
        else:
            type_entity = add_type_to_api(entity['type'], token)
            typeId = str(type_entity['id'])

        main_type = types_url + typeId + '/'
        payload = {
            "name": entity['text'],
            "main_type": main_type,
        }

        # Add fields if they exist in the entity data from Alchemy API
        if 'disambiguated' in entity:
            if 'subType' in entity['disambiguated']:
                sub_types = []
                for sub_type in entity['disambiguated']['subType']:
                    sub_type_id = None
                    if sub_type in types:
                        sub_type_id = types[sub_type]['id']
                    else:
                        subtype_entity = add_type_to_api(sub_type, token)
                        sub_type_id = subtype_entity['id']
                    sub_types.append(
                        types_url + str(sub_type_id) + '/')
                payload['sub_types'] = sub_types
            if 'yago' in entity['disambiguated']:
                payload['yago'] = entity['disambiguated']['yago']
            if 'dbpedia' in entity['disambiguated']:
                payload['dbpedia'] = entity['disambiguated']['dbpedia']
            if 'freebase' in entity['disambiguated']:
                payload['freebase'] = entity['disambiguated']['freebase']
            if 'website' in entity['disambiguated']:
                payload['website'] = entity['disambiguated']['website']
            if 'geonames' in entity['disambiguated']:
                payload['geonames'] = entity['disambiguated']['geonames']
            if 'geo' in entity['disambiguated']:
                geo_data = entity['disambiguated']['geo'].split(' ')
                if len(geo_data) is 2:
                    payload['geo_lat'] = numerical.truncate(
                        float(geo_data[0]), 7)
                    payload['geo_long'] = numerical.truncate(
                        float(geo_data[1]), 7)
        r = requests.post(base_url + "/entities/",
                          headers=headers, data=json.dumps(payload), verify=False)
        api_entity = r.json()

        # Add the entity to MongoDB to cache for local server
        entity_collection.insert_one(api_entity)
    return api_entity


def add_entityscore_to_api(entity, types, token, api_entity, api_entity_id_added):
    if 'id' in api_entity and api_entity['id'] not in api_entity_id_added:
        headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "authorization": "Bearer " + token
        }
        entity_url = base_url + '/entities'
        entityscores_url = base_url + '/entityscores'

        # Ensure that there are no more than 6 decimal places in 'relevance'
        entity['relevance'] = numerical.truncate(float(entity['relevance']), 5)
        entity['relevance'] = str(entity['relevance'])

        # Check if already added
        entity_name = urllib.unquote_plus(
            entity['text'].encode('utf-8')).decode('utf-8')
        relevance = urllib.unquote_plus(
            entity['relevance'].encode('utf-8')).decode('utf-8')

        count = urllib.unquote_plus(
            entity['count'].encode('utf-8')).decode('utf-8')
        r = requests.get(entityscores_url + "/?entity__name=" + entity_name + '&score=' + str(relevance) + '&count=' + count + '&222',
                         headers=headers, verify=False)
        entityscore = r.json()
        api_entityscore = None
        if entityscore['count'] > 0:
            api_entityscore = entityscore['results'][0]
        else:
            api_entity_id = entity_url + '/' + str(api_entity['id']) + '/'
            payload = {
                "entity": api_entity_id,
                "score": entity['relevance'],
                "count": entity['count'],
            }
            r = requests.post(base_url + "/entityscores/",
                              headers=headers, data=json.dumps(payload), verify=False)
            api_entityscore = r.json()

        api_entity_id_added.append(api_entity['id'])
        api_entityscore = entityscores_url + \
            '/' + str(api_entityscore['id']) + '/'
        return (api_entityscore, api_entity_id_added)
    return None


def add_entityscore_to_articles_api(article, api_entityscores, token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    payload = {
        "entities_processed": True,
        "entity_scores": api_entityscores
    }

    r = requests.put(base_url + "/articles/" + str(article['id']) + '/',
                     headers=headers, data=json.dumps(payload), verify=False)
    api_article = r.json()

    return api_article
