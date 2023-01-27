import col
import time
import colorama
''' if the program failed to work that means you have to
    import colorama using
    pip install colorama
'''
from colorama import Fore

#print(Fore.RED + 
print(''' 
                        Welcome
                        -------
      ''')
def home():
    print('what is your name')
    name=input('>>> ')

    print('what color do you want to color your name?')
    print('''
         CHOOSE ANY OF THE OPTION FOR COLOR SELECTION
      |---------------------|       ---INSTRUCTION---
       Enter [1] for Red:
      |---------------------|    To choose an option you 
                OR               have to enter a number 
      |---------------------|    for that option.
       Enter [2] for Blue:       And press enter.
      |---------------------|
                OR
      |---------------------|    S
       Enter [3] for Green:       T
      |---------------------|      R
                OR                  A
      |---------------------|        I
       Enter [4] for Yellow:          G
      |---------------------|          H
                OR                      T   > Straightlearn
      |---------------------|          L
       Enter [5] for Magenta:         E
      |---------------------|        A
                OR                  R
      |---------------------|      N 
       Enter [6] for white:
      |---------------------|
                OR
      |---------------------|   This program was brought 
       Enter [7] for Cyan:      coded by straightlearn 
      |---------------------|   using python on tarmux.
 ''')
    try:
        num=int(input('>>> '))
    except Exception:
        print('program ended because of wrong input')
        quit()

    col.col(num,name)

    try:
        choice=int(input('''
            Would you want to run program afresh
            [1] for yes:
            [2] for No:
            '''))
        if choice==1:
            home()
        elif choice==2:
            print('Ok bye bye')
        else:
            print('bye',name)
    except Exception:
        print('seems like you puted a wrong value')
home()
print('straightlearn skillup')
