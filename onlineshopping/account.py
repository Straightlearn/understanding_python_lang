#for account opening
def acctUpdate(nam=0,ag=0,gend=0,ctry=0,usrna=0):
    if nam ==0:
        print("you need to open account first\n")
        acct()
    elif nam != 0:
        info={"name ":nam,"age ":ag,"gender ":gend,"country ":ctry,"username ":usrna}
        b=info
        #for i in b:
           # print(i,end="")
       # print(info.get("name"))

def acct():
    print("Open account with us")
    name=input("Name: ")
    age=int(input("Age: "))
    gender=input("Gender: ")
    country=input("Country: ")
    usrname=input("Username: ")
    acctUpdate(name,age,gender,country,usrname)
    p=name(name)
    username(usrname)
    country(country)
#acctUpdate()
acct()

#for sending info to main file
def country(con):
    return con
def name(nam):
    return nam
def username(usrn):
    return usrn
