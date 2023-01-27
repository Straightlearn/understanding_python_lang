def your_names(firstname,middlename,lastname):
    print('\nyour names:')
    print('firstname[',firstname,']')
    print('middlename[',middlename,']')
    print('lastname[',lastname,']')

print('what are your names')
firstN=input('Firstname: ')
middN=input('Middlename: ')
lastN=input('lastname: ')
names={"firstname":firstN,"lastname":lastN,"middlename":middN}

#using kwargs to call the function
your_names(**names)
