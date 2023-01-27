import colorama
from colorama import Fore

def col(num,name):
    if num==1:
        print(Fore.RED + name)
    elif num==2:
        print(Fore.BLUE + name)
    elif num==3:
        print(Fore.GREEN + name)
    elif num==4:
        print(Fore.YELLOW + name)
    elif num==5:
        print(Fore.MAGENTA + name)
    elif num==6:
        print(Fore.WHITE + name)
    elif num==7:
        print(Fore.CYAN + name)
    else:
        print('sorry number',num,'is not among the options')
        print('you try again')
