import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

api_key = "73029d91af1a554d2e781b9fb6643a0a"
city = "London"
print(get_weather(city, api_key))