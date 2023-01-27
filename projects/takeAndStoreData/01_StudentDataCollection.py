import time
import json

time=time.ctime(time.time())

print('{:->59}'.format('-'))
print("\nwelcome to Federal university of technology")
print("give us the following info\n")

print("personal data")
firstName=input("[1] FirstName: ")
middleName=input("[2] MiddleName: ")
lastName=input("[3]LastName: ")

def regnum():
    try:
        regnumb=int(input("[4] Regnumber: "))
        return regnumb
    except Exception:
        print("enter a correct value")
        regnum()

regnumb=regnum()

def Age():
    try:
        age=int(input("[5] Age: "))
        return age
    except Exception:
        print("put a valid number")
        Age()

age=Age()
sex=input("[6] Sex: ")
email=input("[7] Email: ")
Religion=input("[8] Religion: ")
sponsor=input("[9] Sponsor: ")
father=input("[10] Father: ")
mother=input("[11] Mother: ")
marriedOr=input("[12] married or single: ")
print("\nGames and hubbies")
Games=input("[1] Games: ")
hubby=input("[2] Hubby: ")

data={


        "Student_name":[
                        {"Firstname":firstName},
                        {"MiddleName":middleName},
                        {"LastName":lastName},
                       ],
        "Age":age,
        "RegNumber":regnumb,
        "Sex":sex,
        "Religion":Religion,
        "Sponsor":sponsor,
        "Father":father,
        "Mother":mother,
        "Marrital_status":marriedOr,
        "GamesAndHubbies":[
                           {"Games":Games},
                           {"Hubby":hubby},
                          ],
        "Registration_DateTime":time,
     } 

#sending student data to school Database
with open("03_StudentsDatabase.json",mode="a") as file:
    json.dump(data,file,indent=4)

#sending student data to latest registration database
with open("02_latestRegistration","w") as f:
    json.dump(data,f,indent=4)


print(firstName,"we have collected and stored your data")
print('have a nice day')


