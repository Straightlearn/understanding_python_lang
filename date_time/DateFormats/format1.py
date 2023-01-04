import datetime

current_date=datetime.date.today()
print('Todays date in different formats is ')
"""he strftime allows you to specify datetime format"""
print(current_date.strftime('%d %b %Y'))
print('or')
print(current_date.strftime('%A %B %Y'))
print('or')
print(current_date.strftime('%a %b %y'))
print('or')
print(current_date.strftime('%Y %b %d'))
print('or')
print('you display using any format you wish')
