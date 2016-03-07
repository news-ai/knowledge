import external.alchemy as alchemy


def entity_extract(article):
    # alchemy_response = alchemy.get_alchemy_url_entities(request.text)
    alchemy_response = alchemy.get_alchemy_url_entities(article['url'])
    print json.dumps(alchemy_response)

    if alchemy_response['status'] == 'OK':
        language = alchemy_response['language']
        entities = alchemy_response['entities']
