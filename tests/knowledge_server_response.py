from grpc.beta import implementations
from grpc import framework
import knowledge_pb2


def test_response():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = knowledge_pb2.beta_create_KnowledgeManager_stub(channel)
    try:
        response = stub.EntityExtraction(knowledge_pb2.EntityRequest(topic='fish'), 10)
        print response.response
    except framework.interfaces.face.face.ExpirationError:
        print 'Expiration error!'

test_response()
