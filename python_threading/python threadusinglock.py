import threading
import time
lock = threading.Lock()

j=0
def threadname():
    try:
        lock.acquire()
        global j
        j=j+1
        current_object=threading.current_thread()
        name=current_object.getName()
        print("%s thread is start and value of j:%d"%(name,j))
        print("%s thread is stop and value of j:%d"%(name,j))    
    finally:
        lock.release()
        pass


list_data=(1,2,3)
if __name__ == '__main__':
    for i in list_data:
        t = threading.Thread(name=i,target=threadname)   
        t.start()
    print("main loop exit")