import unittest

from knowledge.external import yago


class GoogleAPI(unittest.TestCase):

    def setUp(self):
        self.response = yago.get_aida('Orange')

    def testformatVersion(self):
        assert 'formatVersion' in self.response
