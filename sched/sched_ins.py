# Python program  

import sched 
import time 
  
# Creating an instance of the 
# scheduler class 
scheduler = sched.scheduler(time.time,  
                            time.sleep) 
