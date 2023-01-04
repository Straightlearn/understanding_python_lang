import os
def file_path(filename):
    path=os.path.abspath(filename)
    print(path)

print('{:^59}'.format("welcome lets help you find the file pathname"))
filename=input("whats the name of the file ")
file_path(filename)
