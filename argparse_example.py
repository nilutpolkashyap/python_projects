import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required = True, help = "enter your name")
ap.add_argument("-s", "--surname", required = True, help = "enter your surname")
ap.add_argument("-a", "--age", help = "enter your age")
ap.add_argument("-c", "--country", required = True, help = "enter your country") 

args = vars(ap.parse_args())

print("Name: ", args["name"], args["surname"])
print("Age: ", args["age"])
print("Country: ", args["country"])
