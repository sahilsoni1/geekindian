import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_data(name):
    print ('EVENT:', time.ctime(time.time()), name)

print ('START TIME:', time.ctime(time.time()))
scheduler.enter(5, 2, print_data, ('one',)) # print after 5 second
scheduler.enter(7, 1, print_data, ('two',)) # print after 7 second

# Run all scheduled events. This method 
# will wait (using the delayfunc() function 
# passed to the constructor) for the next 
# event, then execute it and so on until there 
# are no more scheduled events.
scheduler.run()  
print('FINISH')
