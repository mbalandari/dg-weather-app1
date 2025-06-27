from django.shortcuts import render
from environs import Env

env = Env()
env.read_env()

def home(request):
    import json
    import requests

    KEY = env.str("KEY")

    if request.method == "POST":
        location = request.POST["location"]
        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=" + KEY + location + "&aqi=no")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        return render(request, "home.html", {"api": api})
        
    else:
        api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=" + KEY + "Berlin&aqi=no")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        return render(request, "home.html", {"api": api})


def about(request):
    return render(request, "about.html")
