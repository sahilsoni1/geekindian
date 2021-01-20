import sched
import threading
import time

scheduler = sched.scheduler(time.time, time.sleep)

# Set up a global to be modified by the threads
counter = 0

def run_sched():
	while 1:
		if(not scheduler.empty()):
			scheduler.run()
		else:
			time.sleep(1)

def increment_counter(name):
    global counter
    print ('EVENT:', time.ctime(time.time()), name)
    counter += 1
    print ('NOW:', counter)

print ('START TIME:', time.ctime(time.time()))
e1 = scheduler.enter(4, 1, increment_counter, ('E1',))
e2 = scheduler.enter(4, 1, increment_counter, ('E2',))

# Start a thread to run the events
t = threading.Thread(target=run_sched)
t.start()

# Back in the main thread, cancel the first scheduled event.
time.sleep(2)
#scheduler.queue return the list of scheduler
if e2 in scheduler.queue :# e2 is exist than cancel
	scheduler.cancel(e2)
	print("Now E2 is cancel.")

time.sleep(6)
print ('E3 Start TIME:', time.ctime(time.time()))
e3 = scheduler.enter(10, 1, increment_counter, ('E3',))#after 10 second