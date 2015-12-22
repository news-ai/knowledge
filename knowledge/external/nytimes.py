import json
import os
import urllib
import requests


# Constructing the New York Times URI structure
# Based on: http://developer.nytimes.com/docs/semantic_api
def construct_uri_structure(query, concept, api_key):
    base_url = '/' + concept + '/'
    if concept is 'name':
        if query['concept_type'] not in ['nytd_geo', 'nytd_org', 'nytd_des']:
            return False
        if not query['specific_concept']:
            return False
        base_url += query['concept_type'] + '/' + query['specific_concept']
    elif concept is 'uri':
        if not query['concept_uri']:
            return False
        base_url += query['concept_uri']
    elif concept is 'article':
        if not query['article_uri']:
            return False
        base_url += query['article_uri']
    else:
        return False
    params = {
        'fields': 'all',
        'api-key': api_key,
    }
    base_url += '.json?' + urllib.urlencode(params)
    return base_url


def get_nytimes_semantic(query, concept):
    api_key = os.getenv('NEWSAI_NYTIMES_SEMANTIC_API', '')
    service_url = 'http://api.nytimes.com/svc/semantic/v2/concept'
    params = construct_uri_structure(query, concept, api_key)
    if params:
        url = service_url + params
        response = requests.get(url).json()
        return response
    else:
        return False

print get_nytimes_semantic({'concept_type': 'nytd_des', 'specific_concept': 'Baseball'}, 'name')
