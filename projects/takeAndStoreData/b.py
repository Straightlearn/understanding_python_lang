import pathlib
import json
import time


#getting and storing date for backup
current_time=time.ctime(time.time())
delTime={"Backup dateTime":current_time}


def databaseFile():
    with open("03_StudentsDatabase.json","r") as DatabaseFile:
        backupData= json.load(DatabaseFile)
        #using the patlib module to delete the file
        print('deleting file.................'*5)
        print(backupData)
        file = pathlib.Path("03_StudentsDatabase.json")
        file.unlink()
        print("The file (03_StudentsDatabase.json) was deleted")


print('Database Deletion\n ')
print('Are you sure you want to delete the database')
try:
    choice=int(input('1 for yes , 2 for no >> '))
except Exception:
    print('you typed a wrong value')
    quit()

if choice ==1:
    print('Please if you procede now you cant reverse the process')
    choice2=int(input('1 for procede, 2 to cancel')
    if choice2==1:
        try:
            databaseFile()
            print("database was deleted because",reason)
            print('Delete time >>>',delTime)
        except Exception:
            print('it seems like you dont have the file')
    else:
        print('deletion canceled
