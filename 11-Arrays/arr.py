colors=['blue','green','black','yellow','brown']
print('main array')
''' this an array of strings, created with python list
'''
#makung a deep copy of the array colors
colors_backUp=colors[:]
print(colors)
print('Length of the array ',len(colors))

del colors[3]
print('\ndeleted value at index 3 of main array')
print(colors)
print('Length of the array ',len(colors))

print('\nremoving blue')
colors.remove('blue')
print(colors)
print('Length of the array ',len(colors))

colors.pop(0)
print('\npoped out value at index 0')
print(colors)
print('Length of the array ',len(colors))

print('\nprinting the backup array')
print(colors_backUp)
print('Length of the array ',len(colors_backUp))

