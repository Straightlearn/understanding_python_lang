Codes=(666,62282,8822)
print('we created a',type(Codes),'data structure with the name Codes')

print('structure of the tuple',Codes)
print('iterating the tuple')
for code in Codes:
    print(code)

#trying to change the value at the zeroth index of the
#tuple Codes
try:
    codes[0]=66
except Exception:
    print('tuples are immutable')
