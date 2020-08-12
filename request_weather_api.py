import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"Rio de Janeiro%2Cbr"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "2fa5f48f9amshe5ed37209260d45p1f9405jsn101f2bd4fa76"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)