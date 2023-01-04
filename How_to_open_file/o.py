'''The aim of this program is to take a file and search and print its content,if the file is empty , or is not found it should handle the errors'''
import os

file=input("put the name of file to open and read ")

#To check if file is empty
check_file = os.stat(file).st_size

#To open the file and store it 
obj=open(file)
try:
    if (check_file==0):
        obj.close()
        print('file has been opened, but is empty')
    else:
        print(obj.read())
        obj.close()
        print("\nThe file is opened,printed and closed")
except FileNotFoundError:
    print('{:>59}'.format("\noops there is no such file in your directory"))
    print('{:-^59}'.format("make sure you have the file ")) 
