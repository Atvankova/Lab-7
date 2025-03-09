import json
import requests


city_name = "Урюпинск"
key = "2380bfe4dae352f1b75e45e5f4532721"
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric")
result = json.loads(response.text)
weather = result['weather'][0]['description']
temperature = result['main']['temp']
humidity = result['main']['humidity']
pressure = result['main']['pressure'] * 1000 // 1333


print(f"Погода в городе {city_name}:")
print(f"Описание: {weather}")
print(f"Температура: {temperature}°C")
print(f"Влажность: {humidity}%")
print(f"Давление: {pressure} мм рт. ст.")
