# Stdlib imports
import json
import urllib
import urllib2
import unicodedata

# Third-party app imports
from newspaper import Article

service_url = 'https://gate.d5.mpi-inf.mpg.de/aida/service/disambiguate'


def get_aida(query):
    query = unicodedata.normalize('NFKD', query).encode('ascii', 'ignore')
    data = urllib.urlencode({
        'text': query,
    })
    response = urllib2.urlopen(url=service_url, data=data).read()
    response = json.loads(response)
    return response


def get_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    return get_aida(article.text)
