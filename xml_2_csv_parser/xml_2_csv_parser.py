import pandas as pd
import xml.etree.ElementTree as ET


# filename = 'songs'
filename = input("Enter name of the XML file (without .xml extension): ")
tree = ET.parse(filename+'.xml')


root = tree.getroot()
element_dict =  {}

for elem in root.iter():
    element_dict[elem.tag]=[]

for elem in root.iter():
    if elem.text=='\n':
        element_dict[elem.tag].append(elem.attrib)
    else:        
        element_dict[elem.tag].append(elem.text)
      
    
def make_list(dict_list, placeholder):
    
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [placeholder] * (lmax - ll)
    
    return dict_list


ans = make_list(element_dict,-1)
df = pd.DataFrame(ans)
print(df)
df.to_csv(filename+".csv")

