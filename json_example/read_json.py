import json

# Open the JSON file
with open('test.json', 'r') as f:
  # Load the JSON data into a Python dictionary
  data = json.load(f)

# Access and use the data
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])

# Print hobbies as a comma-separated string
print("Hobbies:", ", ".join(data["hobbies"]))

# Loop through pets and print their information
for pet in data["pets"]:
  print(f"Pet name: {pet['name']}, type: {pet['type']}, breed: {pet['breed']}")
