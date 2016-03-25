# Stdlib imports
import time
import json
import urllib

# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Imports from app
from middleware import config
from .external.readabilityapi import get_readability_url

# Removing requests warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = config.BASE_URL


def author_extraction(article, types, token):
    api_authors = []
    readability_article = get_readability_url(article['url'])

    if readability_article['author']:
        author = readability_article['author'].title()
        publisher = article['publisher']['name']
        print author, publisher


def article_improve(article, types, token):
    if len(article['authors']) is 0:
        author_extraction(article, types, token)
    return article
