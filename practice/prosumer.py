from threading import Thread, current_thread, Condition
import time
queue = []
condition = Condition()

def producer():
    n = 0
    while True:
        condition.acquire() 
        time.sleep(1)
        if(len(queue) > 0):
            condition.wait()
        n += 1
        queue.append(n)
        print("produced: ", n)
        condition.notify()
        #condition.wait()
        condition.release()

def consumer():
    while True: 
        condition.acquire()
        time.sleep(1)
        if len(queue) == 0:
            condition.wait()
        print("consumed: ", queue.pop())
        condition.notify()
        condition.release()

p = Thread(target = producer, name = 'producer')
c = Thread(target = consumer, name = 'consumer')
p.start()
c.start()