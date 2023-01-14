import os

'''this function checks if a file exists or not. if the file do not exist the the os.path.exists will return false, if not it will return true'''
def check(file_name):
    # Check if file exist or not using the file name
    return os.path.exists(file_name)

print('{:^59}'.format('This program checks if a file exists.And print True or False if it exists or not respectively'))
print('\n')

#taking filename from the user and storing it 
filename=input('input the file to check ')

#send filename to function and printing its return type
print(check(filename))

