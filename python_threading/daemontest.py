from threading import Thread
def sam():
    while True:
    	print("HI")


x=Thread(target=sam)
x.setDaemon(True)
x.start()
time.sleep(2)