import requests

astros = requests.get("http://api.open-notify.org/astros.json")
data_astros = astros.json()
print astros.headers
print astros.content
list(data_astros.values())
list(data_astros.keys())
for item in data_astros['people']:
    print item["name"]
