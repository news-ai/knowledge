from grpc.beta import implementations
from grpc import framework

import knowledge_pb2
import time


class Knowledge(knowledge_pb2.BetaKnowledgeManagerServicer):

    def Topic(self, request, context):
        return knowledge_pb2.TopicReply(response='bye')


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
