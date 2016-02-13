import json

class Entity(object):

    def __str__(self):
        return json.dumps(self.entity_to_dict())

    def to_dict(self):
        return self.__dict__

    def __init__(self):
        super(Entity, self).__init__()

        # Basic information about the tweet
        self.name = ""
        self.description = ""
        self.url = []
        self.type = []
        self.metadata = {}

    @classmethod
    def from_alchemy_api(cls, alchemy_entity):
        entity = cls()
        entity.name = alchemy_entity['text']
        entity.type = alchemy_entity['type']

        if alchemy_entity.has_key('disambiguated'):
            entity.metadata = alchemy_entity['disambiguated']

        return entity;