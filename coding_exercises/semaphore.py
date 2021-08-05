import threading
import time
sem = threading.Semaphore()

global s 
s = 2
def thing1():
   
    time.sleep(1)
    s = s + 3
    sem.release()
    

def thing2():
    
    print(s)







t = threading.Thread(target = thing1)
t.run()
t1 = threading.Thread(target = thing2)
t1.run()
