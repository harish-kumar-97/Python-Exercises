import threading
import time

# defining the main function
def myfunction():
    "function to be executed"
    print("Start a thread")
    time.sleep(3)
    print("End a thread")
    
# define an empty list of threads
threads = []

# Runs 5 concurrent sessions of myfunction()
for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()  # starting the thread
    threads.append(th)
    
# waiting for all the threads to be terminated
for th in threads:
    th.join()