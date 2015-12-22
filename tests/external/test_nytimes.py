import unittest

from knowledge.external import nytimes


class YagoAPI(unittest.TestCase):

    def setUp(self):
        self.response = nytimes.get_nytimes_semantic(
            {'concept_type': 'nytd_des', 'specific_concept': 'Baseball'}, 'name')

    def testSemanticAPI(self):
        assert 'status' in self.response
