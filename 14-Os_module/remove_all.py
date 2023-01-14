import os
import datetime
current_time=datetime.datetime.now()

print("\nDeleting all the files ending with a '.example' file extension")

print("you cant recover the directories if you delete it")
print('\nshould i proceed: 1 for yes , 2 for no')
try:
    choice=int(input('>>> '))
except Exception:
    print('you typed a wrong number')
    quit()

if choice==1:
    print('\nSomething bad will happen if you dont make the right choice')
    print('Are you sure of this: 1 for yes, 2 for no')
    choice2=int(input('>>> '))
    if choice2==1:
        try:
            os.remove('*.example')
            print(current_time.strftime('directories deleted at %d %b %Y - %H:%M'))
        except Exception:
            print('You dont have such directories')
            print('or maybe they are not empty')
    elif choice2==2:
        print("program terminated")
    else:
        print('wrong value')
        quit()
elif choice==2:
    print("We stoped the program")
    print("Nothing was deleted")
else:
    print('wrong value selected')
