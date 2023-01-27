import json

#Decoding a json file
with open("01-family.json","r") as f:
    familyData=json.load(f)

print("below a json file")
print(familyData)
