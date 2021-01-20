import threading, queue
import time
q = queue.LifoQueue()

def worker():
    while True:
        item = q.get()

        print('Working on'+ str(item))
        print('Finished '+str(item))
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print(q.full())
print(q.qsize())
print(q.empty())
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')