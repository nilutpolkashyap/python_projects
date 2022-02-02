import requests
import json
import time
import math

api = "KCL2BN6MRRUJT8ZM9WT8RJVMQ"

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
url2 = "?unitGroup=metric&key="
url3 = "&contentType=json"

city_name = input("Enter city name : ")

complete_rain_url = url + city_name + url2 + api + url3

print(complete_rain_url)

response = requests.get(complete_rain_url)

x = response.json()
y = x["days"]
z = y[1]

rain = z["precip"]

print(rain)