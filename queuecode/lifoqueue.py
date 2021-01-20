import threading, queue
import time
q = queue.LifoQueue()

def consumer():
    while True:
        item = q.get()
        time.sleep(0.5)
        print('Working on'+ str(item))
        time.sleep(0.5)
        print('Finished '+str(item))
        q.task_done()


def producer():
    for item in range(20):
        q.put(item)

print('All task requests sent\n', end='')
threading.Thread(name='consumer',target=consumer).start()
threading.Thread(name='producer',target=producer).start()
# block until all tasks are done
q.join()
print('All work completed')