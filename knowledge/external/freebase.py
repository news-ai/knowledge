# Third-party app imports
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def get_freebase_data(entity):
    freebase = requests.get(entity)
    freebase = freebase.json()
    print freebase
