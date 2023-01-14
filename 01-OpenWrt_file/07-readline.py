print('Let help you read particular lines in your file')

#taking the file name
print("Name of file to read")
file=input('>>> ')

#taking the file number
print('Number of line to read')
num=int(input('>>> '))

with open(file) as file:
    print(file.readline(num*59))
    #the readline function takes bit as parameter


