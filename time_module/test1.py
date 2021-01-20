import time
# return structure time string
# If t is not provided, the current 
# time as returned by localtime() is used.
test1=time.asctime()
print(type(test1))
print(test1)
# https://www.geeksforgeeks.org/python-time-clock_gettime-method/

test2=time.ctime()
print(type(test2))
print(test2) 

test3=time.monotonic()
print(test3)
test4=time.ctime(test3)
print(test4)
time.sleep(1)
print(time.perf_counter())
#
test5=time.gmtime()
test6=time.mktime(test5)
test7=time.localtime()
test8=time.mktime(test7)

print(test5)
print(test7)
print(test7.tm_year)
print(test5.tm_year)
print(test6)
print(test8)