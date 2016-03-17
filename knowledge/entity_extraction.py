import json
import urllib

import requests

import external.alchemy as alchemy

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
        types_url = base_url + '/types/'
        main_type = types_url + str(types[entity['type']]['id']) + '/'
        payload = {
            "name": entity['text'],
            "main_type": main_type,
        }

        # Add fields if they exist in the entity data from Alchemy API
        if 'disambiguated' in entity:
            if 'subType' in entity['disambiguated']:
                sub_types = []
                for sub_type in entity['disambiguated']['subType']:
                    sub_types.append(
                        types_url + str(types[sub_type]['id']) + '/')
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
                    payload['geo_lat'] = geo_data[0]
                    payload['geo_long'] = geo_data[1]
        r = requests.post(base_url + "/entities/",
                          headers=headers, data=json.dumps(payload), verify=False)
        api_entity = r.json()
    return api_entity


def add_entityscore_to_api(entity, types, token, api_entity):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    entity_url = base_url + '/entityscores'

    # Check if already added
    entity_name = urllib.unquote_plus(
        entity['text'].encode('utf-8')).decode('utf-8')
    relevance = urllib.unquote_plus(
        entity['relevance'].encode('utf-8')).decode('utf-8')
    count = urllib.unquote_plus(
        entity['count'].encode('utf-8')).decode('utf-8')
    r = requests.get(entity_url + "/?entity__name=" + entity_name + '&score=' + str(relevance) + '&count=' + count + '&222',
                     headers=headers, verify=False)
    entityscore = r.json()
    api_entityscore = None
    if entityscore['count'] > 0:
        api_entityscore = entityscore['results'][0]
    else:
        api_entity_id = entity_url + str(api_entity['id']) + '/'
        payload = {
            "entity": api_entity_id,
            "score": entity['relevance'],
            "count": entity['count'],
        }
        r = requests.post(base_url + "/entityscores/",
                          headers=headers, data=json.dumps(payload), verify=False)
        api_entityscore = r.json()

    api_entityscore = entity_url + '/' + str(api_entityscore['id']) + '/'
    return api_entityscore


def add_entityscore_to_articles_api(article, api_entityscores, token):
    headers = {
        "content-type": "application/json",
        "accept": "application/json",
        "authorization": "Bearer " + token
    }

    print api_entityscores

    payload = {
        "entities_processed": True,
        "entity_scores": api_entityscores
    }

    r = requests.patch(base_url + "/articles/" + str(article['id']),
                      headers=headers, data=json.dumps(payload), verify=False)
    print r
    api_article = r.json()
    return api_article


def entity_extract(article, types, token):
    alchemy_response = alchemy.get_alchemy_url_entities(article['url'])

    if alchemy_response['status'] == 'OK':
        language = alchemy_response['language']
        entities = alchemy_response['entities']
        api_entityscores = []
        for entity in entities:
            single_entity_api = add_entity_to_api(entity, types, token)
            api_entityscores.append(add_entityscore_to_api(
                entity, types, token, single_entity_api))
        print add_entityscore_to_articles_api(article, api_entityscores, token)
