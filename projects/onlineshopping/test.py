num1=1
num2=2
fruits={"appple":450,"banana":600}

#main code for the home view
def home():

    print("list of fruits in the shope")
    print("[1]Apple  [2]Banana")
    choice=int(input("- "))
    if choice== num1:
        pick1=int(input("Do you want to buy the apple?\n[1]yes.       [2]No.\n "))
        if pick1==num1:
             #function will be here
             print("nn")
        elif pick1==num2:
            print("order canceled")
            home()
        #else:
            #continue
    elif choice==num2:
        pick2=int(input("Do you want to buy the banana?\n[1]yes.        [2]No.\n "))
        if pick2==num1:
            #function will be here
            print("nnnz")
        elif pick2==num2:
            print("order canceled")
            home()
        #else:
            print("please chooce a correct option")
           # continue
home()

amount=int(input("input amount: "))
