import pathlib
import json
import time


#getting and storing date for backup
current_time=time.ctime(time.time())
backupTime={"Backup dateTime":current_time}


def databaseFile():
    #Opening and storing the student database in the obj str data
    with open("02_StudentDatabase.json","r") as DatabaseFile:
        backupData= json.load(DatabaseFile)
    return backupData

#backup function
def backup(backupTime):
    try:
        backupData=databaseFile()
        #opening backup file and backing up file in it
        with open("04_StudentDatabaseBackup.json","a") as BackupFile:
            #To append a newline
            BackupFile.write("\n\n\n")
            json.dump(backupData,BackupFile,indent=5)
            json.dump(backupTime,BackupFile)
    except Exception:
        raise
        print("sorry you dont correctly have a database file")
 



print("Are you sure you want to clear the whole database")
print("1 for yes, 2 for no")
choice=int(input(">>> "))
if choice==1:
    choice2=int(input("1 to continue, 2 to cancel "))
    if choice2==1:
        try:
            #backing up using backup function
            backup(backupTime)
            #using the patlib module to delete the file
            print('deleting file.................'*5)
            print(backupData)
            file = pathlib.Path("02_StudentDatabase.json")
            file.unlink()
            print("The file (04_StudentDatabaseBackup.json) was deleted")
        except Exception:
            raise
            print("an error occured")
            print("Maybe data base is empty already or doesnt exists")
    else:
        print("operation canceled")
        quit()
else:
    print("Nothing was deleted")
    quit()
