#!/usr/bin/python3
'''  function that reads n lines of a text file (UTF8) and prints it to stdout
'''


def read_lines(filename="", nb_lines=0):
    ''' function: read_lines
    '''
    if filename == "" or type(filename) != str:
        return
    if type(nb_lines) != int:
        return
    counter = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                counter += 1
                if nb_lines <= 0 or (counter <= nb_lines and nb_lines > 0):
                    print(line, end='')
                else: 
                    break
    except Exception:
        return 'no file'

print('Text file reader')
texfile=input('\n input name of file to read')
obj=read_lines(textfile)


if obj=='no file':
    print('no such file')
else: 
    pass


