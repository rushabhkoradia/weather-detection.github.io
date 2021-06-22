import requests
#import os
from datetime import datetime

api_key = '6c722c0845751d925d3777e630a8d85f'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y || %I:%M:%S %p")

with open("weather.txt", "w") as f1:
  f1.write("---------------------------------------------------------")
  f1.write("\nWeather Stats for - " + location.upper() + " || " + date_time)
  f1.write("\n---------------------------------------------------------")
  f1.write("\nCurrent temperature: {:.2f} deg C".format(temp_city))
  f1.write("\nCurrent weather desc: " + weather_desc)
  f1.write("\nCurrent Humidity: " + str(hmdt) + " %")
  f1.write("\nCurrent wind speed: " + str(wind_spd) + " kmph")
f1.close()

f2 = open("weather.txt", "r")
print("\nReading File Data . . . . . \n\n")
while True:
    weather_data = f2.readline()
    if not weather_data:
        break
    print("{}".format(weather_data.strip()))
f2.close()
