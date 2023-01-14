#creating an empty list
scores=[]

#using years() to take number of years to take maths
def years():
    try:
        years=int(input("how many years are you taking maths "))
        return years
    except Exception:
        print('only number is allowed')
        years()

#function to take choice
def choice():
    try:
        choice=int(input(':- '))
        return choice
    except Exception:
        print('\n that was a wrong value')
        choice()

#program starts running from here
print('{:^59}'.format('University Maths Scores Record List'))
name=input('hey dear whats your name ')
print('\n',scores,"your list is empty you have no scores yet")
Years=years()
print(name,'You are taking maths for',Years,'years')

for year in range(Years):
    pre_yr=year+1
    print('\n','Put your score for the year',year+1)
    yearnum=int(input('Score in number: '))
    scores.insert(year,yearnum)


print('\nhi',name,'let me help you do some calculation')
print('firstly the list of scores you provided is',scores)
print("hope that's correct. [1]yes. [2]No.")

Choice=choice()
#we continue later

