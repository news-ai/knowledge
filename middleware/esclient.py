from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

from .config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION

host = 'search-elastic-news-p43g5t3yo7pjesbyhois4diva4.us-west-2.es.amazonaws.com'
awsauth = AWS4Auth(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, 'es')

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print(es.info())