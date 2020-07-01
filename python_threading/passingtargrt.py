import threading
import time
def threadlocation():
    location=threading.__file__
    time.sleep(2)
    print("location of threading module is%s"%location)
    return

if __name__ == '__main__':
    t = threading.Thread(target=threadlocation)
    t.start()
    print("main loop exit")

