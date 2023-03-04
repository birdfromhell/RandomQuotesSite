import json

import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": "fe7ac125c5msh94f9c196609b1eep12fb18jsndc6f9e5920c3",
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

x = json.dumps(response.json())
z = json.loads(x)
w = z['originator']

print(w['name'])
