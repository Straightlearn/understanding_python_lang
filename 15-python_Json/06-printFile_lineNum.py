#!/usr/bin/python3
''' function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    ''' function: number_of_lines
    '''
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                counter += 1
        return counter
    except Exception:
        return 0

print('Program To Print Number Of Lines In A File')
print('\nPls put the file, to print number of its lines')
fileName=input('>>> ')


lineNum=number_of_lines(fileName)

if lineNum==0:
    print('sorry the file [',fileName,'] do not exist')
else:
    print('[',fileName,'] has ',lineNum,'line(s)')

