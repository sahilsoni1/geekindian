import os.path
import time
def split_fully(path):    
    parent_path, name = os.path.split(path)    
    if name == "":
        return (parent_path, )    
    else:
        return split_fully(parent_path) + (name, )  

def print_dir(dir_path):    
    for name in os.listdir(dir_path):        
        print(os.path.join(dir_path, name)) 

def print_tree(dir_path):    
    for name in os.listdir(dir_path):        
        full_path = os.path.join(dir_path, name)        
        print(full_path)        
        if os.path.isdir(full_path):            
            print_tree(full_path) 
def print_dir_info(dir_path):    
    for name in os.listdir(dir_path):        
        full_path = os.path.join(dir_path, name)        
        file_size = os.path.getsize(full_path)        
        mod_time = time.ctime(os.path.getmtime(full_path))        
        print("%-32s: %8d bytes, modified %s" % (name, file_size, mod_time)) 
if __name__ == '__main__':
    print(split_fully(os.getcwd()))
    print(print_dir(os.getcwd()))
    print(print_tree(os.getcwd()))
    print_dir_info(os.getcwd())