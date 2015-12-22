import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

from keyspace import KEYSPACE


class Entity(Model):
    __keyspace__ = KEYSPACE
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(required=True)

    def validate(self):
        super(Entity, self).validate()

    def add(**kwargs):
        return Entity.create(name=kwargs['name'])
