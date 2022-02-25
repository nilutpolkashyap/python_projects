crop_name_list = ['wheat','sugarcane','mustard','gram','pea','lentil','linseed','cotton','apple','pearl millet','finger millet','ground nut',
                'soyabean','napier grass','jute','chickpea','sunn hemp','cabbage','watermelon','raddish','cauliflower',]
soil_type_list = ['clayey loamy','loamy','sandy loamy','sandy clayey','sandy clayey','loamy','clayey loamy','black alluvial','loamy','sandy loamy',
                'clayey loamy','sandy loamy','clayey loamy','clayey loamy','clayey loamy','sandy loamy','sandy loamy','sandy loamy',
                'sandy loamy','sandy loamy','loamy',]
season_list = ['rabi','kharif','rabi','rabi','rabi','rabi','rabi','kharif','rabi','kharif','kharif','kharif','kharif','kharif','kharif','rabi',
                'kharif','rabi','rabi','rabi','rabi',]

min_optimum_ph = [6,6.5,6,6,6,6,5,5.8,5.5,7.3,5,6.5,5.8,6.8,4.8,5.5,5,6.5,6.5,5.5,5.5,]
max_optimum_ph = [7,7.5,7.5,7.5,8,7.5,7,8,6.5,7.9,5.3,7,6.2,7.2,5.8,8,8.4,6.8,7.5,7,6.5,]
min_temp = [16,20,18,25,22,18,20,29,21,30,28,25,28,25,24,21,20,15,25,18,17,]
max_temp = [22,32,25,35,25,30,25,34,24,35,33,30,33,31,37,26,35,21,30,25,23,]
min_rainfall = [25,145,60,60,45,15,70,85,100,40,50,50,55,95,160,60,40,40,25,100,40,]
max_rainfall = [75,155,100,75,55,50,75,110,125,50,90,60,60,105,200,90,100,60,35,225,60,]

def common_member(a, b):
    result = [i for i in a if i in b]
    return result

# print(len(crop_name_list))
# print(len(soil_type_list))
# print(len(season_list))
# print(len(min_optimum_ph))
# print(len(max_optimum_ph))
# print(len(min_temp))
# print(len(max_temp))
# print(len(min_rainfall))
# print(len(max_rainfall))


soil_type = input("Enter soil type : ")
print(soil_type)
season = input("Enter season : ")
print(season)
ph = float(input("Enter value of pH : "))
print(ph)
temp = int(input("Enter temperature (in degree celsius) : "))
print(temp)
rainfall = int(input("Enter amount of rainfall (in cms) : "))

crop_list1 = []

for i in range(len(season_list)):
    if season_list[i] == season:
        crop_list1.append(crop_name_list[i])

# print(crop_list1)

crop_list2 = []

for i in range(len(soil_type_list)):
    if soil_type_list[i] == soil_type:
        crop_list2.append(crop_name_list[i])

# print(crop_list2)

recom_crop_list1 = common_member(crop_list1, crop_list2)
# print(recom_crop_list1)

crop_list3 = []

for i in range(len(crop_name_list)):
    if (min_optimum_ph[i] < ph) and (max_optimum_ph[i] > ph):
        crop_list3.append(crop_name_list[i])

# print(crop_list3)

recom_crop_list2 = common_member(recom_crop_list1, crop_list3)
# print(recom_crop_list2)

crop_list4 = []

for i in range(len(crop_name_list)):
    if (min_temp[i] < temp) and (max_temp[i] > temp):
        crop_list4.append(crop_name_list[i])

# print(crop_list4)

recom_crop_list3 = common_member(recom_crop_list2, crop_list4)
# print(recom_crop_list3)

crop_list5 = []

for i in range(len(crop_name_list)):
    if (min_rainfall[i] < rainfall) and (max_rainfall[i] > rainfall):
        crop_list5.append(crop_name_list[i])

# print(crop_list5)

recom_crop_list4 = common_member(recom_crop_list3, crop_list5)
print("*********************************************************")
print("List of recommended crops for given conditions is : ")
print("***************")
print(*recom_crop_list4, sep = "\n")
print("***************")

