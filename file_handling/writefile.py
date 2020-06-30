import os
def make_test_file():
	"""
	It helps to create the text file
	in same folder. if file is exist than
	delete privious data and write new data.
	"""
	a=open('test.txt',"w")
	a.write("This is how you create a new text file.\n")
	a.close()
def make_another_file():
	"""
	It helps to create the text file
	in same folder. if file is exist than
	just  print the message.
	"""
	if os.path.isfile("test.txt"):    
		print("You are trying to create a file that already exists!")  
	else:    
		f=open("test.txt","w")    
		f.write("This is how you create a new text file")
		f.close()
		

def add_more_data():
	f =open("test.txt",'a')
	f.write("A line is adding in exsiting file.\n")
	f.close()
def add_multiple_data_lines():
	f =open("test.txt",'a')
	f.write(
	"""
	here 
	is 
	more text
	""")
	f.close()
def print_test_file():
	a=open("test.txt","r")
	text=a.read()
	print(text)
	a.close()
	del a

def print_line_lenghts():
	a=open("test.txt","r")
	text=a.readlines()
	print(type(text))
	print(text)
	for line in text:
		print(len(line))	

if __name__ == '__main__':
	print(make_test_file.__doc__)
	make_test_file()
	make_another_file()
	add_more_data()
	add_multiple_data_lines()
	print_test_file()
	print_line_lenghts()

