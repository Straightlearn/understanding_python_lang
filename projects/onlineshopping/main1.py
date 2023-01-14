#import shop_items as shtems
class details:
    def __init__(self,nam,ag,gend,ctry,pswd):
        self.name=nam
        self.age=ag
        self.gender=gend
        self.country=ctry
        self.password=pswd
    def printi(self):
        print('{:=>59}'.format("="))
        print('{:^59}'.format("ACCOUNT INFORMATION"))
        print('{:=>59}'.format("="))
        print("*Name: [",self.name,"]")
        print("*Age: [",self.age,"]") 
        print("*Gender: [",self.gender,"]")
        print("*Country: [",self.country,"]")

#codes for data colletion for account opening
print('{:=>59}'.format("="))
print('{:^59}'.format("WELCOME TO CONFIDENCE ONLINE SHOPE"))
print('{:=>59}'.format("="))
print("To continue open an account")
nam=input("Name: ")

"""using exception and error for the age, to handle #error when user puts any character instead of int"""
while True:
    try:
        ag=int(input("Age: "))
        break
    except ValueError:
        print("please put age in number")
gend=input("Gender: ")
ctry=input("Country: ")
psswd=input("password: ")
#sending data to the class
cand1=details(nam,ag,gend,ctry,psswd)
print('{:->59}'.format("-"))
print('{:^59}'.format("Account creation sucessful"))
print('{:->59}'.format("-"))
print("[1]ACCOUNT INFO.",'{:^59}'.format("[2]Shope list.")) 
choice=int(input(" "))
if choice==1:
    print("input your password ")
    passwd=input(" ")
    if passwd==psswd:
        cand1.printi()
    else:
        print("wrong password")
        pass
elif choice==2:
    print("other choice")
    #shtems.items()
 


