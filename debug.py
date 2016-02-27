import knowledge.external.alchemy as alchemy
from knowledge.models.entity import Entity
import middleware.esclient as es
import knowledge.external.google as google

alch_resp = alchemy.get_alchemy_url_entities("http://www.bloomberg.com/bw/articles/2014-12-18/chinese-banks-lure-deposits-by-offering-goodies-for-cash")
entity = Entity.from_alchemy_api(alch_resp['entities'][0])
es_resp = es.write_entity(entity)

print google.get_google_knowledge('Orange')
