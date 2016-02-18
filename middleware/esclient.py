from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

from .config import ELASTIC_USER, ELASTIC_PASSWORD

host = 'knowledge-elastic-1.newsai.org'

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

def write_entity(entity):
	doc = entity.to_dict()
	res = es.index(index="entities", doc_type="entity", id=1, body=doc)
	print res

