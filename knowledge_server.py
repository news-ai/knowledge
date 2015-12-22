from grpc.beta import implementations
from grpc import framework

import knowledge_pb2
from knowledge import entity_extraction
import time


class Knowledge(knowledge_pb2.BetaKnowledgeManagerServicer):

    def EntityExtraction(self, request, context):
        response = entity_extraction.entity_extract(request)
        return knowledge_pb2.EntityReply(response=response)


def serve():
    knowledge_server = knowledge_pb2.beta_create_KnowledgeManager_server(
        Knowledge())
    knowledge_server.add_insecure_port('[::]:50051')
    knowledge_server.start()
    print 'Knowledge server has started'

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        knowledge_server.stop(0)

if __name__ == '__main__':
    serve()
