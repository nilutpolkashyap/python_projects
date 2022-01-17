import requests
import json
import time
import math

sigma = 4.903e-9    # stefan-boltzmann constant
solar_constant = 1367        # solar constant
incoming_solar = 1            # incoming solar radiation
albedo_cons = 1
sea_elevation = 1

api_key = "*****REPLACE WITH API KEY*****"
 
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"

city_name = input("Enter city name : ")
 
complete_weather_url = weather_url + "appid=" + api_key + "&q=" + city_name
complete_forecast_url = forecast_url + "appid=" + api_key + "&q=" + city_name
 
weather_response = requests.get(complete_weather_url)
forecast_response = requests.get(complete_forecast_url)

x = weather_response.json()
y = x["main"]

current_temperature = y["temp"] - 273

temp_max = current_temperature
temp_min = current_temperature

current_humidity = y["humidity"]

humid_max = current_humidity
humid_min = current_humidity
 
if x["cod"] != "404":
 
    while(True):
        weather_response = requests.get(complete_weather_url)
        forecast_response = requests.get(complete_forecast_url)

        x = weather_response.json()

        y = x["main"]
    
        current_temperature = y["temp"]
        current_temperature = current_temperature - 273

        if current_temperature > temp_max:
            temp_max = current_temperature

        if current_temperature < temp_min:
            temp_min = current_temperature

        current_humidity = y["humidity"]

        if current_humidity > humid_max:
            humid_max = current_humidity

        if current_humidity < humid_min:
            humid_min = current_humidity
    
        current_pressure = y["pressure"]        # Atmospheric pressure
    
        z = x["wind"]                           
        wind_speed = z["speed"]                 # Wind speed

        print("*****************************************************")
        print(" Temperature (in degree Celsius) = " + str(current_temperature) +
            "\n Atmospheric Pressure (in hPa unit) = " + str(current_pressure) +
            "\n Humidity (in percentage) = " + str(current_humidity) +
            "\n Wind Speed (in meter/seconds) = " +  str(wind_speed))

        print(" Temp max: ", temp_max)
        print(" Temp min : ", temp_min)

        print(" Humidity max: ", humid_max)
        print(" Humidity min : ", humid_min)

        # Mean Temperature
        mean_temp = (temp_max + temp_min)/2

        delta_num = (4098 * (0.6108 * math.exp((17.27 * mean_temp)/(mean_temp + 237.3))))
        delta_den = (mean_temp + 273.3) ** 2
        # Slope vapour pressure curve
        delta = delta_num / delta_den

        print("Slope Vapour pressure curve : ", delta)

        e_tmax = 0.6108 * math.exp((17.27 * temp_max)/ (temp_max + 237.3))
        e_tmin = 0.6108 * math.exp((17.27 * temp_min)/ (temp_min + 237.3))
        # Saturation Vapour Pressure
        e_S = (e_tmax + e_tmin) / 2  

        print("Saturation vapour pressure : ", e_S)

        # Actual Vapour pressure
        e_A = ((e_tmin * (humid_max/100)) + (e_tmax * (humid_min/100))) / 2

        print("Actual Vapour pressure : ", e_A)

        # Net outgoing long wave solar radiation
        outgoing_radiation = sigma * ((((temp_max + 273.16) ** 4) + ((temp_min + 273.16) ** 4)) / 2) * (0.34 - (0.14 * (e_A ** (1/2))))


        Rav = 1
        R = 1

        # Ra, Extraterrestial radiation
        et_radiation = solar_constant * ((Rav / R) ** 2)

        day = 12             # Day of year
        b = 2 * math.pi * (day / 365)



        Z = 1
        E = 1
        clear_sky_radiation = (0.75 + (2 * E * 10e-5 * Z))



        aS = 0.25
        bS = 0.5

        actual_sunshine = 1
        max_sunshine = 1

        R_s = (aS + bS * (actual_sunshine / max_sunshine)) * et_radiation


        net_solar = (1 - albedo_cons) * incoming_solar

        net_radiation = net_solar - outgoing_radiation
        
        time.sleep(5)
 
else:
    print(" City Not Found ")
