import json
import os
import urllib


def get_google_knowledge(query):
    api_key = os.getenv('NEWSAI_GOOGLE_KNOWLEDGE_API', '')
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    for element in response['itemListElement']:
        print element['result']['name'] + ' (' + str(element['resultScore']) + ')'
    return response
