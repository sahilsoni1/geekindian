import threading
import time
import random
j=0
def threadname(randomtime):
    current_object=threading.current_thread()
    name=current_object.getName()
    time.sleep(randomtime)
    global j
    j=j+1
    print("%s thread is start and value of j:%d"%(name,j))
    time.sleep(randomtime)
    print("%s thread is stop and value of j:%d"%(name,j))    
 
list_data=(1,2,3)
if __name__ == '__main__':
    for i in list_data:
        t = threading.Thread(name=i,target=threadname,args=(random.randrange(0,4,1),))   
        t.start()
    print("main loop exit")