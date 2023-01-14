import info
print("==============================================")
print("welcome to Confidence online shope")
print("==============================================")

#for account opening
print("Open account with us")
name=input("Name: ")
age=input("Age: ")
gender=input("Gender: ")
country=input("Country: ")
username=input("Username: ")

#module for password set up and storing it in passwd
passwd=info.password()
print(f"your password is {passwd}")
#module to print a welcome messege
info.printi(username,gender)

#the online shope
fruits=["orange","banana"]
baprice=500
choice=input("which fruits do you want to buy ")
if choice in fruits:
    print(f"we have {choice} the price is {baprice}")

