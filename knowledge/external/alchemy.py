# Stdlib imports
import json
import os
import urllib

# Third-party app imports
from alchemyapi import AlchemyAPI

alchemyapi = AlchemyAPI()


def get_alchemy_text_entities(query):
    params = {
        'outputMode': 'json',
        'disambiguate': 1,
        'structuredEntities': 1
    }
    response = alchemyapi.entities('text', query, params)
    return response


def get_alchemy_url_entities(query):
    params = {
        'outputMode': 'json',
        'disambiguate': 1,
        'structuredEntities': 1
    }
    response = alchemyapi.entities('url', query, params)
    return response
