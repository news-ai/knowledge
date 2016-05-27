# Stdlib imports
import sys
sys.path.insert(0, '../knowledge')

# Imports from app
from knowledge.external.yago import get_article_text

url = 'http://www.nytimes.com/2016/05/27/us/politics/donald-trump-global-warming-energy-policy.html'

yago_data = get_article_text(url)
print yago_data

for entity in yago_data['mentions']:
    if 'bestEntity' in entity:
        best_entity = entity['bestEntity']
        name = best_entity['kbIdentifier']
        metadata = yago_data['entityMetadata'][name]

        entity_name = metadata['readableRepr']
        entity_url = metadata['url']
        entity_score = best_entity['disambiguationScore']
