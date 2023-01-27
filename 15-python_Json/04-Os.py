import os

with open("05-myfile.txt",mode="w",encoding="utf-8")as file:
    file.write("this the first line\nhere is the second line\nam third line")


with open("05-myfile.txt",mode="r")as file:
    print(file.read())

print("\nThe opened and red filename is",file.name)
print("opened in",file.mode,"mode")
print("file is closed:",file.closed)
