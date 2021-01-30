#   coding: utf-8
from django.shortcuts import render
import requests
from .extras import (
    Weather,
    weatherInfos
)  

from .forms import CityForm

params = {
        'access_key': 'eeb513546914bd969adf810889f895a9',
        'query': 'vitoria',
    }

# Create your views here.
def home(request):
    return render(request,'base.html')
    

def search(request):
    cityName = ""
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            cityName = form.cleaned_data['name']

            params['query'] = cityName

            api_result = requests.get('http://api.weatherstack.com/current', params)
            api_response = api_result.json()
            weather = weatherInfos(api_response)

    return render(request,'weather.html',{'form': weather})