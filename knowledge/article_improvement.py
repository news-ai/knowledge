# Stdlib imports
import time
import json
import urllib

# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Imports from app
from middleware import config

# Removing requests warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = config.BASE_URL


def article_improve(article, types, token):
    print article
    return article
