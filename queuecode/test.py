from queue import Queue,PriorityQueue 
  
# Initializing a queue 
q = PriorityQueue(maxsize = 3) #  size of queue is 3
# Adding of element to queue
print(q.maxsize)
list_data=['sahil','ravish','rajat','ajay']  
for x in list_data:
	if q.full():
		print("%s is not add in queue because it is full"%x)
		break;
	q.put((x)) #add element in queue
 
print("\nElements dequeued from the queue") 
for x in range (int(q.qsize())):#Return the number of items in the queue
	item = q.get()#
	print(item)
	q.task_done()#tells the queue that the processing on the task is complete

if q.empty():
	print("queue is now empty")