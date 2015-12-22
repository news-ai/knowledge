import unittest

from knowledge.external import google


class GoogleAPI(unittest.TestCase):

    def setUp(self):
        self.response = google.get_google_knowledge('Orange')

    def testElement(self):
        assert 'itemListElement' in self.response
