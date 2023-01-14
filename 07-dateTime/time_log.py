import datetime


def log_time(function):
    function()
    def time():
        log_time=datetime.datetime.now()
        print('{:>59}'.format(log_time.strftime('Log_date >>> %a-%b-%Y | Log_time >>> %I:%M %P.')))
        print('{:>59}'.format(f'{"-"*51}'))
    return time


def details():
    name=input('Name: ')
    try:
        age=int(input('Age: '))
    except Exception:
        print('you inputed a wrong value')
        print('start again')
        details()
        blood=input('your blood group: ')

    print('your name:',name)
    print('your age:',age)
    print('name given:',name,'\nage given:',age)
    choice=input('Are those correct> y or n: ')
    if choice == 'y' or choice== 'Y':
        print('{:^59}'.format('Thank you for the information'))
    elif choice =="yes" or choice== "Yes":
        print('{:^45}'.format('Thank you for the information'))
 
    elif choice =='No'or'no':
        print('okey fill form again')
        details()
    elif choice == "no" or "No":
        print('okey fill form again')
        details()
    else:
        print('your input is not valid')
        details()

#execution starts here
print('{:-^59}'.format("FEDERAL MEDICAL CENTRE OWERRI"))
print('{:>59}'.format('Online patient data collection')) 
print('{:->59}'.format("-"))

obj=log_time(details)
obj()
