import threading, queue
import random,time

q = queue.PriorityQueue(maxsize=50)

def student_data():
    while True:
        item = q.get()
        print(item)
        q.task_done()

# turn-on the worker thread
threading.Thread(target=student_data, daemon=True).start()


student_name=['sahil','rajat','ajay','shubham','ravish','avish']
surname=['soni','kumar','suri','anand','mahajan']

student_list=[(x,y) for x in student_name for y in surname ]
# print(student_list)
for item in student_list:
    item_priority=random.randrange(1,20,1)
    q.put((item_priority,item))
print('All task requests sent\n')

# block until all tasks are done
q.join()
print('All work completed')