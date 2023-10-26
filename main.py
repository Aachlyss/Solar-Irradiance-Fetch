import requests

#FREE API KEY - DOESNT WORK ANYMORE FOR FREE
API_KEY = "ccfdb4b005b85109bebed09a341cb674"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    date = input("Enter date (YYYY-MM-DD): ")
    request_url = f"https://api.openweathermap.org/energy/1.0/solar/data?lat={lat}&lon={lon}&date={date}&appid={API_KEY}"
    response = requests.get(request_url)
else:
    print("An error occurred: 1")

if response.status_code == 200:
    data = response.json()
    radial = data['radial']
    print(radial)
else:
    print("An error occurred: 2")