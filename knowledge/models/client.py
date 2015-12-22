import os
os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

import logging

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine import management
from cassandra.cqlengine import ValidationError
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.query import BatchQuery, LWTException

from entity import Oranges


class CassandraClient(object):
    """docstring for CassandraClient"""

    def __init__(self):
        super(CassandraClient, self).__init__()
        self.session = None

    def connect(self, nodes):
        print 'Starting Cassandra'
        cluster = connection.default()
        self.session = cluster

    def sync_model(self):
        log.info("### syncing model...")
        management.sync_table(Oranges)

    def close(self):
        print 'x'