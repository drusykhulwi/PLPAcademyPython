from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    city = request.GET.get('city', 'London')  # Default to London if no city is provided
    api_key = 'b32fd02eb431fe6e9be6d8a8a046d1d3'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return render(request, 'weather/index.html', {'weather': weather_info})
        else:
            return HttpResponse("Error fetching weather data", status=500)

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
