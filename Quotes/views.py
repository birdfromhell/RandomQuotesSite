import json
import requests
from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class QuotesView(View):
    def get(self, request):
        url = "https://quotes15.p.rapidapi.com/quotes/random/"

        headers = {
            "X-RapidAPI-Key": "fe7ac125c5msh94f9c196609b1eep12fb18jsndc6f9e5920c3",
            "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        x = json.dumps(response.json())
        quotes = json.loads(x)
        author = quotes['originator']

        return render(request, 'Quotes/index.html', {
            'Quotes': quotes['content'],
            'Author': author['name']
        })
