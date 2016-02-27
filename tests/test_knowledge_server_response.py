import unittest

from grpc.beta import implementations
from grpc import framework
import knowledge_pb2
import knowledge_server


class KnowledgeServer(unittest.TestCase):

    def setUp(self):
        self.channel = implementations.insecure_channel('localhost', 50051)
        self.stub = knowledge_pb2.beta_create_KnowledgeManager_stub(self.channel)

    def tearDown(self):
        self.channel = None
        self.stub = None

    def testServerConnection(self):
        try:
            response = self.stub.EntityExtraction(knowledge_pb2.EntityRequest(text='who let the catfish out', topic='fish'), 10)
            assert response
        except framework.interfaces.face.face.ExpirationError:
            print 'Expiration error!'
