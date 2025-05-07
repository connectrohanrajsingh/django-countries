from django.shortcuts import render, HttpResponse
from django.views import View
import requests
# Create your views here.


class LandingRequest(View):
    def get(self, request, *args, **kwargs):
        if (kwargs):
            countryName = kwargs['country']
            apiUrl = f"https://restcountries.com/v3.1/name/{countryName}?fullText=true"
            countryDetails = requests.get(apiUrl).json()[0]
            template = "countryinfo/country-info.html"
            context = {'countryDetails': countryDetails}
        else:
            apiUrl = "https://restcountries.com/v3.1/all?fields=name,flags"
            countriesShortInfo = requests.get(apiUrl).json()
            template = "landing/index.html"
            context = {'allCountries': countriesShortInfo}
        return render(request, template, context)
