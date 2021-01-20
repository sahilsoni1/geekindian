import threading
import time
value = 0                    
def Consumer(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s:Running"%name)
    with e:
        e.wait_for(data1)#condition of data1 function

        print("%s:work start"%name)
        time.sleep(4)
        print("%s:work finish"%name)

def Producer(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s:Running"%name)
    
    global value
    value=1  #value of data1 change
    with e:
        time.sleep(4)
        print("notify consumer")
        e.notify(1)


def data1():
    global value
    if value is 1:
        return True
    else:
        return False

if __name__ == '__main__':

    condition = threading.Condition()
    
    t1 = threading.Thread(name='Consumer', 
                          target=Consumer,
                          args=(condition,))
    t1.start()
    t2 = threading.Thread(name='Producer', 
                      target=Producer,
                      args=(condition,))
    
    t2.start()

    