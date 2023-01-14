# Object and Class




## Constructor

A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is called automatically when an object of a class is created. The object is assigned to the class. The aim of using constructor is to initialize the data members of a class.The constructor using the name __init__ . 
Syntax of a constructor:
```
def __init__(self):
	# initializations
```

Intialization, simply means to assign value to something. let say we have a variable called 'name' to intialize it we have to assign value to it. i.e name="straightlearn".intialization in a class is done through constructor methode. in the constructor we have to provide the name 'self' and temporary variables which will hold the values to intialize, as arguwmwnts.
Example:
```
def __init__(self,name,age):
	self.name=name
	self.age=age

```
we can use the above constructor in a class,then when ever we assign the class to an object as an instance of the class, the __init__ method is called automatically.
Example:
```
class StudentData:	
	def __init__(self,name,age,):
		self.name=name
		self.age=age

student_1=StudentData("Straightlearn",26)
student_2=StudentData("John",29)
student_3=StudentData("Joseph",21)
```
checkout code examples in this directory



