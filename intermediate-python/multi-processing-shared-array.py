from multiprocessing import Process, Lock, Value, Array
import time

def add_100(numbers, lock):
  for i in range(100):
    time.sleep(0.1)
    for i in range(len(numbers)):
      with lock:
        numbers[i] += 1


if __name__ == "__main__":
  lock = Lock()
  shared_array = Array('d', [0.0, 100.0, 200.0])

  print(f'Value as start is {shared_array[:]}')

  p1 = Process(target=add_100, args=(shared_array,lock))
  p2 = Process(target=add_100, args=(shared_array,lock))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print(f'Value as start is {shared_array[:]}')

  print(f'End main')
