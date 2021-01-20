import time,os
utc_time=time.gmtime()
print(utc_time)
print('df'+time.asctime(utc_time))


local_time=time.localtime()
print(time.asctime(local_time))


print(time.mktime(local_time))
print(time.mktime(utc_time))

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()
time.localtime()
time.tzname


print(time.strftime("%a, %d %b %Y %H:%M:%S +0000"))
time.strptime("30 Nov 00", "%d %b %y")
# Program
import time
manual_time=time.strptime("30 Nov 00 1 12 34", "%d %b %y %H %M %S")
print(manual_time)
string_format=time.asctime(manual_time)
print('manual_time in string format',string_format)