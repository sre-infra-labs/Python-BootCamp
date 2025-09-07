from multiprocessing import Process, Lock, current_process
from multiprocessing import Queue
import time

def square(numbers,queue,lock):
  for i in numbers:
    with lock:
      queue.put(i*i)
      print(f'\tIn {current_process().name} process with queue size {queue.qsize()}')

def make_negative(numbers,queue,lock):
  for i in numbers:
    with lock:
      queue.put(-i)
      print(f'\tIn {current_process().name} process with queue size {queue.qsize()}')

if __name__ == "__main__":
  print(f"\nStart main")

  q = Queue()
  lock = Lock()
  numbers = range(1,6)

  p1 = Process(target=square, args=(numbers,q,lock))
  p2 = Process(target=make_negative, args=(numbers,q,lock))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print(f'queue size is {q.qsize()}')

  while not q.empty():
    print(q.get())

  print(f"End main")
