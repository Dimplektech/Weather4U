import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

payload = {
    'q': "London",
    'limit': 5,
    'appid': API_KEY
}

response = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=payload)
location = response.json()[0]

print(location['name'])
print(location['lat'])
print(location['lon'])

lat = location['lat']
lon = location['lon']
print(location)