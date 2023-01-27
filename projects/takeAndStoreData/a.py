import pathlib
import json
import time


#getting and storing date for backup
current_time=time.ctime(time.time())
backupTime={"Backup dateTime":current_time}


#Opening and storing the student database in the obj str data
with open("02_StudentDatabase.json") as f:
    backupData=json.load(f)
    print(backupData)
"""
try:
    backupData2=databaseFile()
except Exception:
    raise
    print("database file currently unavailable")

print(backupData)"""

"""
#opening backup file and backing up file in it
with open("04_StudentDatabaseBackup.json","a") as BackupFile:
#To append a newline
BackupFile.write("\n\n\n")
json.dump(backupData,BackupFile,indent=5)
json.dump(backupTime,BackupFile)

 




#backing up using backup function
backup(backupTime)
#using the patlib module to delete the file
print('deleting file.................'*5)
print(backupData)
file = pathlib.Path("02_StudentDatabase.json")
file.unlink()
print("The file (04_StudentDatabaseBackup.json) was deleted")
"""
