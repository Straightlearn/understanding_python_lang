import datetime

current_date=datetime.datetime.now()
print('The time is ')

#for 24 hours time
print(current_date.strftime('%H:%M'),'time in 24 hours format')

print('or')

#for 12 hours time
print(current_date.strftime('%I:%M'),'time in 12 hours format')

print('or')

#adding day/night specifer
print(current_date.strftime('%I:%M %P'),'time in 12 hours format with day/night specifer')

print('or')

#adding minutes and seconds
print(current_date.strftime('%I:%M:%m:%S'),'time in 12 hours format with minutes and seconds')
