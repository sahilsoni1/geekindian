# Program
import time
import os

os.environ['TZ'] = 'US/Eastern'
time.tzset()

print('US/Eastern in string form:',time.asctime()) 

os.environ['TZ'] = 'Australia/Melbourne'
time.tzset()

print('Australia/Melbourne in string form:',time.asctime())

os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()

print('Asia/Kolkata in string form:',time.asctime()) 