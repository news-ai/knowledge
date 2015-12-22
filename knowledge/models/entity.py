import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

from keyspace import KEYSPACE

class Oranges(Model):
    __keyspace__ = KEYSPACE
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at = columns.DateTime()
    description = columns.Text(required=False)

    def validate(self):
        super(Oranges, self).validate()

def add_to_model(type, description):
    sophie = Oranges.create(example_type=1, description='Sophie')
