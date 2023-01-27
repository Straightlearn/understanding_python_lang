import time


epc=time.time()
localTime=time.localtime(epc)
fullTime=time.ctime(epc)

print(localTime)
print(fullTime)
