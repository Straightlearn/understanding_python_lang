file_name=input('please input file name to open: ')


try:
    #using the with keyword to open file
    with open(file_name) as file:
        print('\n......File contents')
        print(file.read())
        print('......File reading ends here')

        #checking if file was closed after reading
        print("\nAm inside the 'with' contruct, is file closed?")
        ans=file.closed
        if ans==True:
            print('yes file is closed\n')
        elif ans==False:
            print("No file is not closed\n")
        else:
            pass
    print("Now am outside the 'with' contruct, is file closed?")
    ans2=file.closed
    if ans2==True:
        print('yes file is closed')
    elif ans2==False:
        print('No file is still open')
except Exception:
    print('The file {} doesnt exits'.format(file_name))

