name=input('Hello am confidene am your python course instructor, whats your name? ')

print("Hi",name)
x=input(" introduce yourself in one sentence, but not a small sentence\n ")

if len(x)>59:
    print('{:>59.59}'.format(x))
    print("\n",name,"should stick to instructions, now you introduction is not conplete")
elif len(x)<=9:
    print('{:59}'.format(name,"Run the program again, your sentence is very poor")) 
else:
    print('{:>59}'.format(x))
    print("\nNot that bad you kept instruction")
