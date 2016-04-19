# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def get_entity_name(entity_url):
    return entity_url.split('/')[-1]


def get_dbpedia_data(entity_url):
    entity_name = get_entity_name(entity_url)

    dbpedia = requests.get('http://dbpedia.org/data/' + entity_name + '.json')
    dbpedia = dbpedia.json()

    resource_name = 'http://dbpedia.org/resource/' + entity_name

    if resource_name in dbpedia:
        if 'http://dbpedia.org/ontology/abstract' in dbpedia[resource_name]:
            print dbpedia[resource_name]['http://dbpedia.org/ontology/abstract']
