from models import client, entity
from datetime import datetime


def entity_extract(request):
    print request.topic
    return 'bye'
