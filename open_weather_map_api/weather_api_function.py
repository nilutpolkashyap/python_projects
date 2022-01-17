import requests, json, time
import math

api_key = "REPLACE WITH API KEY"
 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = input("Enter city name : ")
 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
response = requests.get(complete_url)
 
x = response.json()
 
if x["cod"] != "404":
    
    y = x["main"]

    current_temp = y["temp"] - 273

    temp_max = current_temp
    temp_min = current_temp

    current_humid = y["humidity"]

    humid_max = current_humid
    humid_min = current_humid

    while(True):
    
        current_temp = y["temp"] - 273

        if current_temp > temp_max:
            temp_max = current_temp

        if current_temp < temp_min:
            temp_min = current_temp
    
        current_pressure = y["pressure"]
    
        current_humid = y["humidity"]

        humid_max = current_humid
        humid_min = current_humid

        mean_temp = (temp_max + temp_min)/2

        if current_humid > humid_max:
            humid_max
    
        z = x["wind"]
    
        wind_speed = z["speed"]
        print("*****************************************************")
        print(" Temperature (in degree Celsius) = " + str(current_temp) +
            "\n Atmospheric Pressure (in hPa unit) = " + str(current_pressure) +
            "\n Humidity (in percentage) = " + str(current_humid) +
            "\n Wind Speed (in meter/seconds) = " +  str(wind_speed) +
            "\n Max Temp = " + str(temp_max) + 
            "\n Min Temp = " + str(temp_min) +  
            "\n Max Humid = " + str(humid_max) + 
            "\n Min Humid = " + str(humid_min))

        print("Mean temp = ", mean_temp)

        delta_num = (4098 * (0.6108 * math.exp((17.27 * mean_temp)/(mean_temp + 237.3))))
        delta_den = (mean_temp + 273.3) ** 2
        delta = delta_num / delta_den

        ## Saturation Vapour Pressure
        e_tmax = 0.6108 * math.exp((17.27 * temp_max)/ (temp_max + 237.3))
        e_tmin = 0.6108 * math.exp((17.27 * temp_min)/ (temp_min + 237.3))

        e_S = (e_tmax + e_tmin) / 2    

        


        time.sleep(5)
 
else:
    print(" City Not Found ")
