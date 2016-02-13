import json
import os
import urllib

from middleware import config

def get_alchemy_named_entities(query):
    endpoint = 'http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities'
    params = {
        'apikey': config.ALCHEMY_API,
        'text': query,
        'outputMode': 'json',
        'disambiguate': 1,
        'structuredEntities': 1
    }
    url = endpoint + '?' + urllib.urlencode(params)
    response = json.loads(urllib.urlopen(url).read())
    return response