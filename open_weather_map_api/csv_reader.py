import csv
 
with open('rain_forecast_records.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines == []:
            continue
        else:
            print(lines[0], " : ", lines[1])