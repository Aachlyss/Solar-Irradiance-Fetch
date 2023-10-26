import requests
import jsonpointer
BASE = "https://api.openweathermap.org/energy/1.0/solar/data?lat=60.45&lon=-38.67&date=2023-03-30&appid=ccfdb4b005b85109bebed09a341cb674"
API_KEY = "cae97c7631f17106c7dc24e731a5a890"
lat = 60.45
lon = -38.67
date="2023-03-30"
tz = "+03:00"

request_url1 = f"https://api.openweathermap.org/energy/1.0/solar/data?lat={lat}&lon={lon}&date={date}&appid={API_KEY}"
response1 = requests.get(request_url1)

if response1.status_code == 200:
    data = response1.json()
    print("Hello")
    