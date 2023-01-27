def your_names(firstname,middlename,lastname):
    print('\nyour names:')
    print('firstname[',firstname,']')
    print('middlename[',middlename,']')
    print('lastname[',lastname,']')

print('what are your names')
firstN=input('Firstname: ')
middN=input('Middlename: ')
lastN=input('lastname: ')
names=(firstN,middN,lastN)

#using args to call the function
your_names(*names)
