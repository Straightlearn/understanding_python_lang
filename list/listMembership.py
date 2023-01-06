#creating a list
classList=["uzochi","nmesoma","confidence","john","amaka","deby"]

print('{:^59}'.format('Department of surveying, year two class list'))

print('lets check if your name is in our class list')
name=input('whats your name ')

#checking if name value is in list
if name in classList:
    print('\n',name,'we have your name in the list ')
else:
    print('\n',name,'your name is not in our list')
    print('what we have in our list is',len(classList),'students')
    print('They are:')
 
    for students in classList:
        print(students)

print('\n',name,'do you what us to add your name')
choice=int(input('Press 1 for yes. or 2 for no: '))
if choice==1:
    classList.append(name)
    """adding to the list"""

    #making sure name was added
    if name not in classList:
        print('we couldnt add your name')
    else:
        print('\nYour name was added and list updated')
        print('Updated list')

        #iterating the list
        for students in classList:
            print(students)
        print('we now have total of ',len(classList))
        print('with you being the',len(classList),'student');
elif choice==2:
    print('ok')
else:
    print('The number typed is not required number') 
