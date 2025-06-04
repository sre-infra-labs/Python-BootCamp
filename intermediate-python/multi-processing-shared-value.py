from multiprocessing import Process, Lock, Value, Array
import time

def add_100(number,lock):
  for i in range(100):
    time.sleep(0.01)
    with lock:
      number.value += 1

if __name__ == "__main__":
  shared_number = Value('i',0) # Value(data_type, value)
  lock = Lock()

  print(f'\nValue at start: {shared_number.value}')
  p1 = Process(target=add_100,args=(shared_number,lock))
  p2 = Process(target=add_100,args=(shared_number,lock))

  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print(f'Value at end: {shared_number.value}')

  print('\nEnd main')
