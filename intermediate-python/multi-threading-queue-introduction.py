from threading import Thread, Lock
from queue import Queue
import time

if __name__ == "__main__":

  q = Queue()

  q.put(1)
  q.put(2)
  q.put(3)

  first = q.get()
  print(first)

  # Check if queue is empty?
  # q.empty()

  # When done processing queue task, mark it done
  q.task_done()

  # Block further execution until all kinds in queue ar done processing
  q.join()

  print('end main')