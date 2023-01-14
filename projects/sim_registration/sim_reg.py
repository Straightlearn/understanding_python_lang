class SimReg:
    def __init__(self,*info):
        self.info=info
    def UserData(self):
        print("Sim User Data")  
        print(self.info["name"])


name=input('your name: ')
age=int(input('your age: '))
NIN=int(input("Nin: "))
Country=str(input("Country: "))
info={"name":name,"age":age,"NIN":NIN,"country":Country}
print(info["name"])
print(info["age"])

candi=SimReg(info)
print(candi.play())
