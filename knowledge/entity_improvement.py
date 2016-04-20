# Imports from app
from knowledge.external.freebase import get_freebase_data
from knowledge.external.dbpedia import get_dbpedia_description


def entity_improve(entity, types, token):
    if 'dbpedia' in entity:
        print get_dbpedia_description(entity['dbpedia'])
