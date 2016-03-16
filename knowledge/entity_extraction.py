import json
import urllib

import requests

import external.alchemy as alchemy

base_url = 'https://context.newsai.org/api'


def add_entity_to_api(entity, types, token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    entity_name = urllib.unquote_plus(
        entity['text'].encode('utf-8')).decode('utf-8')
    r = requests.get(base_url + "/entities/?name=" + entity_name,
                     headers=headers, verify=False)
    context = r.json()
    api_entity = None
    if context['count'] > 0:
        api_entity = context['results'][0]
    else:
        api_entity = None

    return api_entity


def add_entityscore_to_api(entity, types, token, api_entity):
    print 'x'


def entity_extract(article, types, token):
    alchemy_response = alchemy.get_alchemy_url_entities(article['url'])

    if alchemy_response['status'] == 'OK':
        language = alchemy_response['language']
        entities = alchemy_response['entities']
        entity_api = {}
        for entity in entities:
            single_entity_api = add_entity_to_api(entity, types, token)
            add_entityscore_to_api(entity, types, token, single_entity_api)
