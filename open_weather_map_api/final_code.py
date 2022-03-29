import requests
import json
import time
import math
from read_kc_values import get_kc_values

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

city_name = input("Enter City Name : ")
# soil_type = input("Enter Soil Type : ")
crop_name = input("Enter Crop Name : ")

# *****Weather Forecast API - OPEN WEATHER MAP*****
weather_api_key = "OPEN_WEATHER_API"
 
weather_url = "http://api.openweathermap.org/data/2.5/weather?"

complete_weather_url = weather_url + "appid=" + weather_api_key + "&q=" + city_name
# print(complete_weather_url)

weather_response = requests.get(complete_weather_url)
x = weather_response.json()


# *****Rain Forecast API - VISUAL CROSSING*****
rain_api_key = "KCL2BN6MRRUJT8ZM9WT8RJVMQ"

rain_url = "VISUAL_CROSSING_API"

complete_rain_url = rain_url + city_name + "?unitGroup=metric&key=" + rain_api_key + "&contentType=json"
# print(complete_rain_url)

# *****KC Values*****
kc_values = get_kc_values(crop_name)
print(kc_values)


if x["cod"] != "404":
    y = x["main"]

    current_temp = y["temp"] - 273

    temp_max = current_temp
    temp_min = current_temp

    current_humid = y["humidity"]

    humid_max = current_humid
    humid_min = current_humid

    while(True):
        # print("Found")

        # *****Weather forecast Data*****
        weather_response = requests.get(complete_weather_url)
        x = weather_response.json()
        y = x["main"]

        current_temp = y["temp"] - 273

        if current_temp > temp_max:
            temp_max = current_temp

        if current_temp < temp_min:
            temp_min = current_temp
    
        current_pressure = y["pressure"]
    
        current_humid = y["humidity"]

        if current_humid > humid_max:
            humid_max = current_humid

        if current_humid < humid_min:
            humid_min = current_humid

        mean_temp = (temp_max + temp_min)/2
    
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
        et_num = (0.408 * delta * (net_radiation - G)) + ((900 / (current_temp + 273) * a2 * (e_S - e_A)) ** (1/2)) 
        et_den = delta + ((1 + 0.34 * a2) ** (1/2))
        eva_transpiration = et_num / et_den
        print(" Evapotranspiration : ", eva_transpiration)



        # *****Rain forecast Data*****
        rain_forecast_response = requests.get(complete_rain_url)
        x1 = rain_forecast_response.json()
        y1 = x1["days"]
        z1 = y1[0]
        rain = z1["precip"]

        print(" Rain : ",rain)


        

        time.sleep(5)

else:
    print("*****Weather data for " + city_name + " NOT FOUND*****")
