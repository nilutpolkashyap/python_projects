import requests
import json
import time
import math
import csv  

api = "********API_KEY********"
filename = "rain_forecast_records.csv"

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
url2 = "?unitGroup=metric&key="
url3 = "&contentType=json"

city_name = input("Enter city name : ")

complete_rain_url = url + city_name + url2 + api + url3

# print(complete_rain_url)

forecast_list = [0,0,0,0,0,0,0]
past_list = [0,0,0]

response = requests.get(complete_rain_url)

x = response.json()
y = x["days"]
# z = y[0] 

forecast_list[0] = y[0]["precip"]
forecast_list[1] = y[1]["precip"]
forecast_list[2] = y[2]["precip"]
forecast_list[3] = y[3]["precip"]
forecast_list[4] = y[4]["precip"]
forecast_list[5] = y[5]["precip"]
forecast_list[6] = y[6]["precip"]

# rain = y[0]["precip"]
print("Today's forecast : {}".format(forecast_list[0]))
print("Future Forecast")
for i in range(1,7):
    print(" Day {} : {}".format(i, forecast_list[i]))

with open(filename, 'w', encoding='UTF8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for i in range(0,3):
        rows = []
        day = i - 3
        csvwriter.writerow(["Day {}".format(day), past_list[i]])

    csvwriter.writerow(["Today", y[0]['precip']])

    for i in range(1,7):
        csvwriter.writerow(["Day {}".format(i),y[i]['precip']])

    

# print(rain)
