import requests
import json

def request_api():
	url = "http://api.openweathermap.org/data/2.5/weather?id=3451189&appid=&units=metric"

	response = requests.request("GET", url)
	return json.loads(response.text)