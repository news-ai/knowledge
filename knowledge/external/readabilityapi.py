from readability import ParserClient

from middleware import config

parser_client = ParserClient(token=config.READABILITY_API)


def get_readability_url(query):
    parser_response = parser_client.get_article(query)
    article = parser_response.json()
    return article
