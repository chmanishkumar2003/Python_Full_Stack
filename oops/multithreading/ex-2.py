#Same code ,but it will first it will prints thread-1 and then thread-2

import time
import threading

def task():
    for i in range(3):
        print(f"[{threading.current_thread().name}] Printing Number: {i}")
        time.sleep(1)
        
def squares():
    for i in range(3):
        print(f"[{threading.current_thread().name}] Squares of thread-1's numbers:{i*i}")
        time.sleep(1)

#Craeting threads
t1=threading.Thread(target=task,name="Thread-1")
t2=threading.Thread(target=squares,name="Thread-2")

t1.start()  # Starting the first thread
t1.join()  # Wait for thread 1 to finish

t2.start()  # Starting the second thread
t2.join()  # Wait for thread 2 to finish

print("Both threads have finished execution")