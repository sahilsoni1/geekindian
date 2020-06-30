import os, os.path 
import re             
def print_pdf (root, dirs, files):   
	for file in files:      
		path = os.path.join (root, file)      
		path = os.path.normcase (path)      
		if re.search (r".*\.py", path):         
			print(path)

for root, dirs, files in os.walk('.'):
	print_pdf(root,dirs,files) 