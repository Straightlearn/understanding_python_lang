import time

name=input('what is your name ')
print('How many seconds do want me to wait before i greet you')
wait=int(input('>>> '))
print('waiting...')
time.sleep(wait)
print('hi ',name,'hope you are good')
print('i waited for',wait,'seconds')
