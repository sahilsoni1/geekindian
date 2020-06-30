import os,shutil
import time
def make_version_path(path,version):
	"""
	it gives version for log file 
	"""
	if version == 0:
		return path
	else:
		return path +"."+str(version)

def rotate(path,version):
	"""
	The  rotate  function uses a technique 
	common in recursive functions
	"""
	old_path =make_version_path(path,version)
	if not os.path.exists(old_path):
		raise IOError("%s doesn’t exist" %path) 

	new_path = make_version_path(path,version +1)
	if os.path.exists(new_path):
		rotate(path,version +1)
	shutil.move(old_path,new_path)
def make_file(file_name):
	"""
	It helps to create the text file
	in same folder. if file is exist than
	delete privious data and write new data.
	"""
	a=open(file_name,"w")#create a file objects
	data_length=a.write(file_name+"This is how you create a new text file.\n")# write data in file 
	print("%d bytes have in %s"%(data_length,file_name))
	a.close()# close the file
	if(os.path.isfile(file_name)):
		return True
	else:
		return False
def rotate_log_file(path):
	if not os.path.exists(path):
		new_file = make_file(path)
		del new_file
	rotate(path,0)

if __name__ == '__main__':
	rotate_log_file("log")