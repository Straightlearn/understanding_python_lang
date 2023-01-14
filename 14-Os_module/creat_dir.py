import os
dirr=os.listdir()

print('press 1 to make a directory or 2 to list directory')

def choice():
    try:
        choice=int(input('>>> '))
        return choice
    except:
        print('must be a number')
        print('press 1 to make a directory or 2 to list directoy')
        choice()

choice=choice()
if choice ==1:
    name=input('Type name of the directory to create: ')
    try:
        os.mkdir(name+'.example')
        print('Directory is has been created')
        dirr1=os.listdir()
        print('Below are list of current directories')
        for i in dirr1:
            print(i)
        print("Straightlearn added a '.example' file extension for some reason")
    except Exception:
        print('Directory already exits')
        print('Below are list of current directories')
        for i in dirr:
            print(i)
elif choice ==2:
    for i in dirr:
        print(i) 
elif choice==None:
    print('nothing was selected')
else:
    print('wrong input')

