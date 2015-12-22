import sys
sys.path.insert(0, '../knowledge')
from knowledge.external import yago

response = yago.get_aida('Orange')
print response
