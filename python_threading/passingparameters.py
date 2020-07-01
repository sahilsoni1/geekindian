import threading
import time
def threadlocation(*args,**kwargs):

	time.sleep(1)
	print("thread start")
	print("thread list:%s"%str(args) )
	print("thread dictionary:%s"%str(kwargs))
	time.sleep(1)
	print("thread stop")
	return
dictionary={"sahil":"soni","rajat":"kumar"}
list_data=(1,2,3)
if __name__ == '__main__':

	t = threading.Thread(target=threadlocation,args=list_data,kwargs=dictionary)	
	t.start()
	print("main loop exit")

