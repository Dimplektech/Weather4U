import requests

API_KEY = "b3df37c2831edc1eb315e526cc84f7ca"

payload = {
    'q': "London",
    'limit': 5,
    'appid': API_KEY
}

respnse = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=payload)