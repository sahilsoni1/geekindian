    import os.path
    import time
    def print_dir_info(dir_path,data):
        
        for name in os.listdir(dir_path):        
            full_path = os.path.join(dir_path, name)        
            file_size = os.path.getsize(full_path)        
            mod_time = time.ctime(os.path.getctime(full_path))        
            # print("%-32s: %8d bytes, modified %s" % (name, file_size, mod_time)) 
            data[os.path.getctime(full_path)]=str(full_path)

    if __name__ == '__main__':
        data={}
        print_dir_info(os.getcwd(),data)
        # print(data)
        for i in sorted (data.keys()) :
            print(i)
            print(data[i]) #sorted file in cureent folder


