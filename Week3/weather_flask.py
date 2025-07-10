import requests
api_key = "09c7f50be3f4672ab55f5e19cd94e773"
city = "Bangalore"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    print(f"City: {weather_data['name']}")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Temp.: {weather_data['main']['temp']}*C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print(f"Failed to get data. Response_code : {response.status_code}")