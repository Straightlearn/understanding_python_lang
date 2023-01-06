john_scores=(["scores"],50,43,87,54)
peter_scores=(["scores"],50,43,87,54)

print("This is peter's scores")
for score in peter_scores:
    print(score)

print("This is john's scores")
for score in john_scores:
    print(score)

print('\ndo peter and john has same scores?')
if peter_scores == peter_scores:
    print('yes peter and john has same scores')

else:
    print('No peter and john has different scores')

print('\npeter and john are they the same?')
if peter_scores is  john_scores:
    print('yes they are the same')
else:
    print('No peter and john are different ')

print('\nIt is confirmed that peter and john has same scores')
print("john's scores:",john_scores)
print("peter's scores:",peter_scores)
print('But peter and john are not the same')
print("peter's id:",id(peter_scores))
print("john's id:",id(john_scores))
