import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_data(name):
    print ('EVENT:', time.ctime(time.time()), name)

print ('START TIME:', time.ctime(time.time()))
now = time.time()
scheduler.enterabs(now+5, 2, print_data, ('first',))
scheduler.enterabs(now+5, 1, print_data , ('second',))

# Run all scheduled events. This method 
# will wait (using the delayfunc() function 
# passed to the constructor) for the next 
# event, then execute it and so on until there 
# are no more scheduled events.
scheduler.run()  
print('FINISH')

