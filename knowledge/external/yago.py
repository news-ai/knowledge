import json
import os
import urllib
import urllib2


def get_aida(query):
    service_url = 'https://gate.d5.mpi-inf.mpg.de/aida/service/disambiguate'
    data = urllib.urlencode({
        'text': query,
    })
    response = urllib2.urlopen(url=service_url, data=data).read()
    response = json.loads(response)
    print response
    return response
