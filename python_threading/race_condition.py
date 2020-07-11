import threading
import time
lock = threading.Lock()

j=0
def test1():
    try:
        lock.acquire()
        global j
        j=j+1
        current_object=threading.current_thread()
        name=current_object.getName()
        
        print("%s thread is start and value of j:%d"%(name,j))
        time.sleep(1)
        print("%s thread is stop and value of j:%d"%(name,j))    
    finally:
        # lock.release()
        pass

if __name__ == '__main__':

    t1 = threading.Thread(name="test1",target=test1) 
    t1.start()
    t1.join()     #wait until function complete the work
    lock.release()# unlock the test1 function

