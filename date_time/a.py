import datetime

#function for age calculation
def age(birthYear,currentYear):
    #age=int(birthYear-currentYear-birt)
    #return age
    try:
        age=int(currentYear-birthYear)
        print(name,'you are',age,'years old')
        return age
    except ValueError:#TypeError:
        print(name,'thats not your real age')

currentTime=datetime.date.today()
currentYear=int(currentTime.strftime('%Y'))
print('{:^59}'.format('SIMPLE PROGRAM TO CALCULATE AGE' ))
name=input('Hello whats your name: ')
birthYear=int(input("What's your birth year: "))
age=int(age(birthYear,currentYear))
if age<20:
    print('your parents must be pround of you')
elif age>20 and age<45:
    print('enjoy your youth')
else:
print('enjoy your elderly age')

