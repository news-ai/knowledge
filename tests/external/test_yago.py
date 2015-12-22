import unittest

from knowledge.external import yago


class YagoAPI(unittest.TestCase):

    def setUp(self):
        self.response = yago.get_aida('Orange')

    def testAidaAPI(self):
        assert 'formatVersion' in self.response
