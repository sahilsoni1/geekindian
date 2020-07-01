import threading
import time
import sys
def threadname(*args):
	current_object=threading.current_thread()
	name=current_object.getName()
	deamon_status=current_object.isDaemon()
	print("%s thread is start,deoman type:%s"%(name,deamon_status))
	time.sleep(1)
	print("%s thread list:%s"%(str(name),str(args)) )
	time.sleep(4)
	print("%s thread is stop"%name)

	return
list_data=(1,2,3)
if __name__ == '__main__':
	for i in list_data:
		t = threading.Thread(name=i,target=threadname,args=list_data)	
		if(i==2):
			t.setDaemon(True)

		t.start()

	
	sys.exit("Age less than 18")
	print("main loop exit")

