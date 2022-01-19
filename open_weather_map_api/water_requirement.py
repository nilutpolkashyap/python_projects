import requests
import json
import time
import math

sigma = 4.903e-9    # stefan-boltzmann constant
solar_constant = 1367        # solar constant
incoming_solar = 1            # incoming solar radiation
albedo_cons = 1
sea_elevation = 1

CP_air = 1.013e-3       # specific heat of air at constant pressure 
MW_air = 0.622          # ratio molecular weight of water vapour 
latent_heat = 2.26      # latent heat of water vapour 

sea_level = 1
E = 1

api_key = "**********API_KEY**********"
 
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

        print(" Slope Vapour pressure curve : ", delta)

        e_tmax = 0.6108 * math.exp((17.27 * temp_max)/ (temp_max + 237.3))
        e_tmin = 0.6108 * math.exp((17.27 * temp_min)/ (temp_min + 237.3))
        # Saturation Vapour Pressure
        e_S = (e_tmax + e_tmin) / 2  

        print(" Saturation vapour pressure : ", e_S)

        # Actual Vapour pressure
        e_A = ((e_tmin * (humid_max/100)) + (e_tmax * (humid_min/100))) / 2

        print(" Actual Vapour pressure : ", e_A)
        
        DOY = 19   # Day of year from january first

        b = 2 * math.pi * (DOY / 365)

        R_ratio = 1.00011 + (0.034221 * math.cos(b)) + (0.00128 * math.sin(b)) + (0.000719 * math.cos(2*b)) + (0.000077 * math.sin(2*b))
        print(" R_av / R : ", R_ratio)

        # Ra, Extraterrestial radiation
        R_a = solar_constant * (R_ratio)
        print(" Extraterrestial Radiation : ",R_a)

        # clear sky solar radiation
        R_s0 = (0.75 + (2e-5 * sea_level)) * R_a

        actual_sunshine = 1
        max_sunshine = 1

        R_s = (0.25 + 0.5 * (actual_sunshine / max_sunshine)) * R_a
        
        print(" Clear skysolar radiation : ", R_s)

        # Net outgoing long wave solar radiation
        R_nl = sigma * ((((temp_max + 273.16) ** 4) + ((temp_min + 273.16) ** 4)) / 2) * (0.34 - (0.14 * (e_A ** (1/2)))) * ((1.35 * (R_s/R_s0) - 0.35))
        
        net_solar = (1 - albedo_cons) * incoming_solar

        net_radiation = net_solar - R_nl
        print(" Net radiation : ", net_radiation)

        # psychromatric constant
        g = (CP_air * current_pressure) / (MW_air * latent_heat)

        G = 1
        a2 = wind_speed

        print(" Psychromatric Constant : ", g)

        # Evapotranspiration
        et_num = (0.408 * delta * (net_radiation - G)) + ((900 / (current_temperature + 273) * a2 * (e_S - e_A)) ** (1/2)) 
        et_den = delta + ((1 + 0.34 * a2) ** (1/2))
        eva_transpiration = et_num / et_den
        print(" Evapotranspiration : ", eva_transpiration)
        
        time.sleep(5)
 
else:
    print(" City Not Found ")
