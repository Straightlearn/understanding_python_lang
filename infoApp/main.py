import info 
print("======================================================")
print("CONFIDENCE ONLINE REGISTRATION FORM")
print("======================================================")
print("please enter your credentials")
finame=input("Firstname: ")
midname=input("Middlename: ")
surname=input("Surname: ")
biyear=input("Birth year: ")
biday=input("Day of birth: ")
bimonth=input("Birth month: ")
country=input("Country: ")
state=input("State of origin: ")
city=input("Residence city: ")

print("Confirm details")
info.names(finame,midname,surname)
info.birthdate(biday,bimonth,biyear)
info.location(country,state,city)

answer=input("is those correct? y/n ")
if answer == "y":
    print("Thanks for the informations")
elif answer == "n":
    print("Refill the forms")
else :
    print("oops something went wrong")
