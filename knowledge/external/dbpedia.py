# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def get_entity_name(entity_url):
    return entity_url.split('/')[-1]


def get_english_from_dict(resource_data):
    for resource in resource_data:
        if resource['lang'] == 'en':
            return resource
    return False


def get_dbpedia_data(entity_url):
    entity_name = get_entity_name(entity_url)

    dbpedia = requests.get('http://dbpedia.org/data/' + entity_name + '.json')
    dbpedia = dbpedia.json()

    resource_name = 'http://dbpedia.org/resource/' + entity_name
    return (dbpedia, resource_name)


def get_dbpedia_description(entity_url):
    dbpedia, resource_name = get_dbpedia_data(entity_url)

    if resource_name in dbpedia:
        if 'http://dbpedia.org/ontology/abstract' in dbpedia[resource_name]:
            resource = get_english_from_dict(
                dbpedia[resource_name]['http://dbpedia.org/ontology/abstract'])
            if resource and 'value' in resource:
                return resource['value']
