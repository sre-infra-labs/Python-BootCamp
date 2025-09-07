from threading import Thread
import time
import os

def square_numbers():
  for i in range(100):
    i*i
    time.sleep(0.5)

num_threads = 10
threads = []

# create threads
for i in range(num_threads):
  t = Thread(target=square_numbers)
  threads.append(t)

# start threads
for t in threads:
  t.start()

# join
for t in threads:
  t.join()

print('end main')


