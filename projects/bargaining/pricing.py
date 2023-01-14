def price():
    print(' i sell the cars for 5000000')
    print('should i write the receipt, 1 for yes 2 for no')
    choice=int(input('>>> '))
    if choice==1:
        pass
        #transfer function call
        #receipt function here call
    elif choice==2:
        print('I really want to sell this car to you')
        print('ok how much are you buying it')
        choice2=int(input('>>> '))
        if choice2 >=4000000:
            print('ok i will sell to you')
            #transfer function call
            #receipt function call
        elif choice2 >3000000 and choice2<4000000:
            print('you tried but add something')
            print('are you adding something,1 for yes 2 for no')
            choice3=int(input('>>> '))
            if choice3==1:
                print('what are you adding to',choice2)
                add=int(input('>>> '))
                pric=choice2+add
                if pric >=3500000:
                    pass
                    #transfer function call
                    #receipt function call
                elif pric <3500000:
                    print('you just dont wan buy')
                    print('how can you price it',pric,'for this model')
                    quit()
                else:
                    pass
            elif choice3==2:
                print('ok thanks')
                quit()
            else:
                pass
        else:
            print(choice2,'is very poor')
    else:
        print('you didnt say something reasonable')
        quit()

price()
