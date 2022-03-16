import csv
 
# with open('kc_values.csv', mode ='r')as file:
#     csvFile = csv.reader(file)
#     for lines in csvFile:
#         if lines == []:
#             continue
#         else:
#             print(lines[0], " -> ", lines[1], " ; ", lines[2], " ; ", lines[3], " ; ", lines[4])

def get_kc_values(crop_name):
    kc_values = []
    with open('kc_values.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines[0] == crop_name:
                kc_values = [lines[0], lines[1], lines[2], lines[3], lines[4]]
                break
    return kc_values        

