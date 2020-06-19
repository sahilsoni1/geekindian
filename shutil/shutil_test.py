import shutil
import os
def make_file(file_name):
	"""
	It helps to create the text file
	in same folder. if file is exist than
	delete privious data and write new data.
	"""
	a=open(file_name,"w")#create a file objects
	data_length=a.write("This is how you create a new text file.\n")# write data in file 
	print("%d bytes have in test.txt"%data_length)
	a.close()# close the file
	if(os.path.isfile(file_name)):
		return True
	else:
		return False

def copy_file(src,dst):
	"""
	copy the source file to destination file
	and it will return Ture if file has 
	copy sucessfully	"""
	name=shutil.copy(src, dst)
	if(os.path.isfile(name)):
		return True
	else:
		return False
def move_rename_file(src,dst):
	if(os.path.isfile(src)):
		name=shutil.move(src,dst)
		print(name)
		if(os.path.isfile(name)):
			return True
		else:
			return False
	else:
		print(src + " source file is not present.")
		print(shutil.which("movetest.txt"))
		return False

if __name__ == '__main__':
#	print(copy_file.__doc__)
#	print(make_file("test.txt"))
#	print(copy_file("test.txt","copytest.txt"))#copy file to file
	print(copy_file("test.txt","copytest.txt"))#work on linux. copy file in parent folder.
#	move_rename_file("copytest.txt","movetest.txt")
	move_rename_file("movetest.txt","../movetest.txt")
