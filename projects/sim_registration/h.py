class SimReg:
    def __init__(self,*info):
        self.info=info
    def play(self):
        return self.info


name=input('your name: ')
age=int(input('your age: '))
NIN=int(input("Nin: "))
Country=(input("Country: "))
info={"name":name,"age":age,"NIN":NIN,"country":Country}
print(info["name"])
print(info["age"])

candi=SimReg(info)
info=(candi.play())
print(info)
