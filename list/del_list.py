#the list
foods=["stew rice","oha soup"]

print('hi am the waiter')
print('what we have in menu are')
for index in foods:
    print(index)

print('those are the foods we have, which one do you want to order')
print('press 1 to remove',foods[0],'or 2 to remove',foods[1])

choice=int(input('>>> '))

if choice==1:
    del foods[0]
    print('you have been served',foods[1])
elif choice==2:
    del foods[1]
    print('you have been served',foods[0])

print('our served food in menu',foods)
