from multiprocessing import Process
import os
import time

processes = []
num_processes = os.cpu_count()

print(f"cpu counts: {num_processes}")

def square_numbers():
  for i in range(100):
    i*i
    time.sleep(0.5)

# Create process
for i in range(num_processes):
  p = Process(target=square_numbers)
  processes.append(p)

# Start process
for p in processes:
  p.start()

# Wait for all processes to finish
for p in processes:
  p.join()

print('end main')

