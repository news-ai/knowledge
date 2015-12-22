import sys
sys.path.insert(0, '../knowledge')
from knowledge.external import google

response = google.get_google_knowledge('Orange')
for element in response['itemListElement']:
    print element['result']['name'] + ' (' + str(element['resultScore']) + ')'