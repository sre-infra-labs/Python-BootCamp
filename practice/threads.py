import time
from threading import Thread, current_thread

class Task(Thread):
    def run(self):
        while True:
            print(current_thread().name, end=" ")
            print('hello', end=" ")
            time.sleep(1)
            print('world')

t1 = Task()
t1.start()
t2 = Task()
t2.start()
t1.join()
t2.join()