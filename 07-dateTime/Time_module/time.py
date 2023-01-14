import time
t = time.time()

time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(t))
'2019-05-27 12:03 CEST'

time.strftime('%Y-%m-%d %H:%M %Z', time.gmtime(t))
'2019-05-27 10:03 GMT'
