from django.shortcuts import render
from requests.exceptions import ConnectionError

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zipcode+"&date=2020-05-16&distance=250&API_KEY=4B92331A-A16B-45CE-A908-7D47C396FA01")

        try:
            api = json.loads(api_request.content)
        except ConnectionError as e:    
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            description = api[0]['Discussion']
            color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            description = api[0]['Discussion']
            color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            description = api[0]['Discussion']
            color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            description = api[0]['Discussion']
            color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            description = api[0]['Discussion']
            color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            description = api[0]['Discussion']
            color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'description': description,
            'color': color
            })
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20005&date=2020-05-16&distance=25&API_KEY=4B92331A-A16B-45CE-A908-7D47C396FA01")

        try:
            api = json.loads(api_request.content)
        except ConnectionError as e:    
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            description = api[0]['Discussion']
            color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            description = api[0]['Discussion']
            color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            description = api[0]['Discussion']
            color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            description = api[0]['Discussion']
            color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            description = api[0]['Discussion']
            color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            description = api[0]['Discussion']
            color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'description': description,
            'color': color
            })



def about(request):
    return render(request, 'about.html', {})