from copy import deepcopy

Asserts=["house","phone","car","laptop"]
Asserts2=deepcopy(Asserts)

print('main list')
for i in Asserts:
    print(i)

print('\ndeep copied list')
for j in Asserts2:
    print(j)

Asserts[1]="sheeps"
Asserts.append('cloths')

if Asserts==Asserts2:
    print('main asserts and copied are same')
else:
    print('their is a change in main list')
    print('main list',Asserts)
    print('copied list',Asserts2)
