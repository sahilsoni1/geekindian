import threading
import time
def threadname(*args,**kwargs):
	current_object=threading.current_thread()
	name=current_object.getName()
	print("%s thread is start"%name)
	time.sleep(1)
	print("%s thread list:%s"%(str(name),str(args)) )
	time.sleep(1)
	print("%s thread is stop"%name)
	return
list_data=(1,2,3)
if __name__ == '__main__':
	for i in list_data:
		t = threading.Thread(name=i,target=threadname,args=list_data)	
		t.start()
	print("main loop exit")

