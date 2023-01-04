class details:
    def __init__(self,nam,ag,gend,ctry,):
        self.name=nam
        self.age=ag
        self.gender=gend
        self.country=ctry
    def printi(self):
        print("=================================")
        print("     ACCOUNT INFORMATION")
        print("=================================")
        print("*Name: [",self.name,"]")
        print("*Age: [",self.age,"]") 
        print("*Gender: [",self.gender,"]")
        print("*Country: [",self.country,"]")

#import account as Acct 

print("======================================================")
print("     WELCOME TO CONFIDENCE ONLINE SHOPE")
print("======================================================")

nam=input("Name: ")
ag=input("Age: ")
gend=input("Gender: ")
ctry=input("Country: ")
cand1=details(nam,ag,gend,ctry)
cand1.printi()
#for account creation
#name=Acct.acct()
#usrnam=Acct.username()
#name=Acct.name()

#print(name,usrnam,name)


