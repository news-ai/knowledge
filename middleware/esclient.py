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
