import time

from grpc.beta import implementations
from grpc import framework

import knowledge_pb2
from middleware import log
from knowledge import entity_extraction
from knowledge.models import client

logger = log.setup_custom_logger('knowledge')


class Knowledge(knowledge_pb2.BetaKnowledgeManagerServicer):

    def EntityExtraction(self, request, context):
        response = entity_extraction.entity_extract(request)
        return knowledge_pb2.EntityReply(response=response)


def serve():
    cassandra_client = client.CassandraClient()
    cassandra_client.connect(['127.0.0.1'])
    knowledge_server = knowledge_pb2.beta_create_KnowledgeManager_server(
        Knowledge())
    knowledge_server.add_insecure_port('[::]:50051')
    knowledge_server.start()
    logger.debug('Knowledge server has started')

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        logger.debug('Knowledge server has stopped')
        knowledge_server.stop(0)

if __name__ == '__main__':
    serve()
