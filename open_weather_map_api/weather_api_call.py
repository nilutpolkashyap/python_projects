import requests, json
 
api_key = "REPLACE WITH API KEY"
 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = input("Enter city name : ")
 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
response = requests.get(complete_url)
 
x = response.json()
 
if x["cod"] != "404":
 
    y = x["main"]
 
    current_temperature = y["temp"]
    current_temperature = current_temperature - 273
 
    current_pressure = y["pressure"]
 
    current_humidity = y["humidity"]
 
    z = x["wind"]
 
    wind_speed = z["speed"]
 
    print(" Temperature (in degree Celsius) = " + str(current_temperature) +
          "\n Atmospheric Pressure (in hPa unit) = " + str(current_pressure) +
          "\n Humidity (in percentage) = " + str(current_humidity) +
          "\n Wind Speed (in meter/seconds) = " +  str(wind_speed))
 
else:
    print(" City Not Found ")
