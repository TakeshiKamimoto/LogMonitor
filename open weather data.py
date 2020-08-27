!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

city = "Tokyo"
key = '793a85e2346507655c6f21d02566d03f'  # your API Key
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&APPID=' + key

print(url)
response = requests.get(url)

print("---")
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)
print("---")
data = json.loads(response.text)
print(city)
print("weather:", data["weather"][0]["main"])
print("temp:", data["main"]["temp"])
print("pressure:", data["main"]["pressure"])
print("humidity:", data["main"]["humidity"])
print("temp_min:", data["main"]["temp_min"])
print("temp_max:", data["main"]["temp_max"])
