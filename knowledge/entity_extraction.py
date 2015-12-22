from models import client, entity
from datetime import datetime
from cassandra.cqlengine.management import sync_table

client = client.CassandraClient()
client.connect(['127.0.0.1'])

def entity_extract(request):
    print request.topic
    return 'bye'
