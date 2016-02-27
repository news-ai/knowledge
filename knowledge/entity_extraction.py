from datetime import datetime

import external.alchemy as alchemy
import models.entity as Entity
import middleware.esclient as es

def entity_extract(request):
	alchemy_response = alchemy.get_alchemy_text_entities(request.text)
	entity = Entity.from_alchemy_api(alchemy_response['entities'][0])
	elastic_response = es.write_entity(entity)
	return elastic_response
