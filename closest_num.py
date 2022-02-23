myList = [4, 1, 88, 44, 3]
myNumber = 40
# takeClosest(myList, myNumber)

val = min(myList, key=lambda x:abs(x-myNumber))
print("value :", val)
