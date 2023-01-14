import os
dirr=os.listdir()

print('press 1 to make a directory or 2 to list directory')

def choice():
    try:
        choice=int(input('>>> '))
        return choice
    except Exception:
        print('you typed a wrong value')
        print('press 1 to make a directory or 2 to list directory')
        choice()

choice=choice()
try:
    if choice ==1:
        name=input('type name of the directory: ')
        try:
            os.mkdir(name)
            print('Directory is created')
            dirr1=os.listdir()
            for i in dirr1:
                print(i)
        except Exception:
            print('Directory already exits')
            for i in dirr:
                print(i)
    elif choice ==2:
        for i in dirr:
            print(i)
    else:
        print('wrong input')
except Exception:
    print('nothing was typed')

