import requests
import json
#r = requests.get('http://localhost:9200')
r = requests.get('http://swapi.co/api/people/')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1

print(i)
