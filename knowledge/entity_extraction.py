# Imports from app
import external.alchemy as alchemy
from internal.context import add_entity_to_api, add_entityscore_to_api, add_entityscore_to_articles_api


def entity_extract(article, types, token):
    alchemy_response = alchemy.get_alchemy_url_entities(article['url'])
    print alchemy_response['status']

    if alchemy_response['status'] == 'OK':
        language = alchemy_response['language']
        entities = alchemy_response['entities']
        api_entityscores = []
        api_entity_id_added = []
        for entity in entities:
            single_entity_api = add_entity_to_api(entity, types, token)

            # This process helps remove duplication from the API.
            # Having a problem.
            api_entityscore = add_entityscore_to_api(
                entity, types, token, single_entity_api, api_entity_id_added)
            if api_entityscore:
                api_entityscores.append(api_entityscore)
        response = add_entityscore_to_articles_api(
            article, api_entityscores, token)
        return response
