import os
dirr=os.listdir()
try:
    os.mkdir('uzo')
    print('Directory is created')
    for i in dirr:
        print(i)
except Exception:
    print('Directory already exits')
    for i in dirr:
        print(i)
