import os
import logging

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'
log = logging.getLogger('knowledge')

from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine import management
from cassandra.cqlengine import ValidationError
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.query import BatchQuery, LWTException

from knowledge.models import entity
import config


class CassandraClient(object):
    """docstring for CassandraClient"""

    def __init__(self):
        super(CassandraClient, self).__init__()
        self.session = None

    def sync_model(self):
        log.info("### Syncing Models...")
        management.sync_table(entity.Entity)

    def connect(self, nodes, keyspace):
        log.info("### Starting Cassandra...")
        self.session = connection.setup(nodes, default_keyspace=config.KEYSPACE)
        self.sync_model()
