import threading
import time
                    
def wait_for_event(e,t):
    current_object=threading.current_thread()
    name=current_object.getName()
    print("%s: thread start"%str(name))
    event_is_set = e.wait(t)
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
    t1 = threading.Thread(name='wait_for_event', 
                      target=wait_for_event,
                      args=(e,2))
    t2 = threading.Thread(name='event_trigger', 
                      target=event_trigger,
                      args=(e,))
    t1.start()
    t2.start()

    