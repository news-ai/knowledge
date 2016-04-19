# Imports from app
from knowledge.external.freebase import get_freebase_data
from knowledge.external.dbpedia import get_dbpedia_data

def entity_improve(entity, types, token):
    get_dbpedia_data(entity['dbpedia'])
