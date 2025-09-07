from threading import Lock, Thread
import time

def process():
    lock = Lock()    
    lock.acquire()
    print("aquired lock", end=" ")
    time.sleep(1)
    lock.release()
    print("released lock")

t1 = Thread(target=process)
t2 = Thread(target=process)
t1.start()
t2.start()

