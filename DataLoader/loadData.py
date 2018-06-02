import requests
import json
import time
from pprint import pprint
from urllib.parse import urlencode
from urllib.request import Request, urlopen

with open('/Users/pratik/Documents/Programming/Python/Projects/IMDB_PROJECT/RestFramework/imdbmovie/restApi/imdb.json') as f:
    data = json.load(f)

url = "http://localhost:8000/movies/"
headers = {'Content-Type':'application/json'}

for d in data:
    d['popularity99'] = d.pop('99popularity','99popularity')
    d['generes']=d.pop('genre','genre')
    print(d)
    request = Request(url, urlencode(d).encode())
    json = urlopen(request).read().decode()
    r = requests.post(url, data=d, verify=False, headers=headers)
    print(r.text)
    time.sleep(60)


#pprint(data)


# url = "http://localhost:8000/movies/"
# headers = {'Content-Type':'application/json'}
# json_data = json.loads('restApi/imdb.json')
# print (json_data)

# r = requests.post(url, data=open('example.json', 'rb'), headers=headers)
#
# with open('data','rb') as payload:
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     r = requests.post('https://IP_ADDRESS/rest/rest/2', auth=('userid', 'password'),
#                       data=payload, verify=False, headers=headers)