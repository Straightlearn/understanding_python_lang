
def printi(name,gender):
    if gender== "male":
        print(f"welcome mr {name}")
    elif gender!= "male":
        print(f"welcome mrs/miss {name}")

def password():
    passwd1=input("choose a password: ")
    passwd2=input("Confirm password: ")
    if passwd1==passwd2:
        print("Account creation successful")

    else:
        print("The password is incorrect")
        password()
    return passwd1

def wallet():
    print("\nplease fund your wallet")
    
