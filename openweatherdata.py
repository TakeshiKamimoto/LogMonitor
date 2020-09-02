# -*- coding: utf-8 -*-

import json
import requests

def readData():
  city = "Tokyo"
  key = '793a85e2346507655c6f21d02566d03'  # your API Key
  url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=' + city + '&APPID=' + key

  #print(url)
  response = requests.get(url)

  print("---")
  data = response.json()

  data = json.loads(response.text)
  t = data["main"]["temp"]
  print("temp:", t)
  p = data["main"]["pressure"]
  print("pressure:", p)
  h = data["main"]["humidity"]
  print("humidity:", h)
  
  return(t, h, p)

if __name__ == '__main__':
    readData()

