import os

def file_check(filename):
    check_file = os.stat(filename).st_size
    if(check_file == 0):
        print("The file is empty.")
    else:
        print("The file is not empty.")


print('{:^59}'.format("lets check if a file is empty or not"))
print("Please make sure the file exists\n")

#taking file name from user
filename=input('input the filename\n ')

try:
    #sending filename to the function
    file_check(filename)
except FileNotFoundError:
    print('     oops The file you typed  doesnt exists in your system')
