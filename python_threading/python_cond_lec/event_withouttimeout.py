import threading
import time
                    
def event(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s: thread start"%str(name))
    print("%s: wait for trigger"%str(name))
    event_is_set = e.wait()
    print("%s:event_active"%str(name))
    time.sleep(3)#perform the work
    print("%s:work_done"%str(name))

def event_trigger(e):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s: thread start"%str(name))
    time.sleep(3)
    print("%s: trigger_activate"%str(name))
    event_is_set = e.set()
    


if __name__ == '__main__':
    e = threading.Event()
    for x in range(3):
        t1 = threading.Thread(name='event'+str(x), 
                          target=event,
                          args=(e,))
        t1.start()

    t2 = threading.Thread(name='event_trigger', 
                      target=event_trigger,
                      args=(e,))
    t2.start()

    