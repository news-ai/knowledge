from nose.plugins import Plugin

from knowledge.external import google

class GoogleAPITest(Plugin):

    def __init__(self):
        self.response = google.get_google_knowledge('Orange')
        print self.response

    def check_itemListElement(self):
        assert 'itemListElemsent' in element

