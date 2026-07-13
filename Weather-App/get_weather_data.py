import requests

city_name = input("Enter city name: ")
API_Key = '9be1ec7c31ecc5879053b2372efab6fa'
weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'


response = requests.get(weather_url)
if response.status_code == 200:
    data = response.json()
    print(f'\n--- Weather Information for {city_name.title()} ---')
    print('Current Weather is', data['weather'][0]['description'])
    print('Temperature is', data['main']['temp'],'°C')
    print('Temperature Feels like', data['main']['feels_like'],'°C')
    print('Humidity is', data['main']['humidity'], '%')
else:
    print(f"Error Occurred! Status Code: {response.status_code}")
    print("Response:", response.text)
