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
    
    if request.method=="POST":

        cityName = request.POST['City']
        params['query'] = cityName
    
        api_result = requests.get('http://api.weatherstack.com/current', params)
        api_response = api_result.json()
        
        if ('error' in api_response):
            msg = "Error, Place data not found."
            return render(request,'error.html', {'form': msg})

        weather = weatherInfos(api_response)
    
        return render(request,'weather.html',{'form': weather})
    
    return render(request,'base.html')