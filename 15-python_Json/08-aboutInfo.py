import json

# Initialize an empty dictionary to store the data
data = {}

# Ask the user for input and store it in the dictionary
name = input("Enter name: ")
age = input("Enter age: ")
address = input("Enter address: ")
data["name"] = name
data["age"] = age
data["address"] = address

# Use the json.dump() function to store the dictionary in a JSON file
with open("data.json", "w") as f:
    json.dump(data, f,indent=4)

print("Data has been successfully stored in data.json file.")

