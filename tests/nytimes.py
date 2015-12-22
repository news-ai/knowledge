import sys
sys.path.insert(0, '../knowledge')
from knowledge.external import nytimes

response = nytimes.get_nytimes_semantic({'concept_type': 'nytd_des', 'specific_concept': 'Baseball'}, 'name')
print response