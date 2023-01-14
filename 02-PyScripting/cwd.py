import os
"""os is a library it stands for operatng system"""

#here we just made a function for gwtting the cwd
def current_wd():
    """os.getcwd is used to get current working directory"""
    cwd=os.getcwd()
    print(cwd)

print('{:^59}'.format("getting the cwd using function we created"))
current_wd() 
print("\n")
print('{:^59}'.format("getting the cwd dirctly without a function"))
cwd=os.getcwd()
print(cwd)
