import requests
import json

endereco = input()

request = requests.get("http://viacep.com.br/ws/" + endereco + "/json/",auth=('',''))
json = json.loads(request.content)

print(type(json))








