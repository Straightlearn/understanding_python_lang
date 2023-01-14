class Robot:
    def __init__(self, name=None,built_year=None):
        self.name = name 
        self.built_year=built_year
    def say_hi(self):#object method
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    """Using getter and setter method"""
    def set_name(self, name):#setter method
        self.name = name
    def get_name(self):#getter method
        return self.name

    def set_built_year(self,built_year):#setter method
        self.built_year=built_year
    def get_built_year(self,):#getter method
        return self.built_year

"""setting the first robot"""
robot1= Robot()#giving the first instance
robot1.set_name("Cp-l20")
robot1.set_built_year(2015)
robot1.say_hi()
print("I was made in the year",robot1.get_built_year())

"""setting the second robot"""
robot2= Robot()#giving the second instance
robot2.set_name(robot1.get_name())
robot2.set_built_year(2020)
print("\nHi I am the second robot with same name",robot2.get_name(),",as the first robot.But I am made in the year",robot2.get_built_year())
