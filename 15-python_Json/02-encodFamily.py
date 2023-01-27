import json

family={
        "father":"Stanley",
        "mother":"Rose",
        "children":{
            "fitstborn":"Emeka",
            "secondborn":"peter",
            "lastborn":"grace",},
        "location":"Owerri",
        "class":"high",
        }


with open("01-family.json","w") as f:
    json.dump(family,f,indent=4,sort_keys=True)
