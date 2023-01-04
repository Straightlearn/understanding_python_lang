class details:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def about(self):
        '''first method'''
        print("\nhi my name is",self.name)
        print("and i am ",self.age,"years old"),
    def remark(self):
        '''second method'''
        print("    ",self.name,'''has successufly conpleted the intro to object and class in python''') 


print('{:^59}'.format('An Intro To Object And Class'))

#Taking name
name=input("whats your name ")

#Taking age making sure age is in integer
while True:
    try:
        age=int(input("whats your age "))
        break
    except ValueError:
        print("your age must be in number")

#p here is an object(instance of the class details
p=details(name,age)

#calling the methods
p.about()
'''first mehod'''
p.remark()
'''second method'''
