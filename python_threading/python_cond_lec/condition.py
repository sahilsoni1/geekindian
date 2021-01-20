import threading
import time
value = 0                    
def Consumer(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s:Running"%name)
    with e:
        print("%s:wait for notification"%name)
        e.wait()
        print("%s:work start"%name)
        time.sleep(4)
        print("%s:work finish"%name)

def Producer(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s"%name)
    global value
    value=1
    with e:
        time.sleep(1)
        print("notify all")
        e.notify_all()


def data1():
    print("trueq1")
    global value
    print(value)
    if value is 1:
        print("true")
        return True
    else:
        return False

if __name__ == '__main__':

    condition = threading.Condition()
    for x in range(4):
        t1 = threading.Thread(name='Consumer'+str(x), 
                          target=Consumer,
                          args=(condition,))
        t1.start()
    t2 = threading.Thread(name='Producer', 
                      target=Producer,
                      args=(condition,))
    
    t2.start()

    