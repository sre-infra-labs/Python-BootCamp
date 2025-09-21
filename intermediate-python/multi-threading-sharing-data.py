from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
  global database_value

  #lock.acquire()
  with lock:
    local_value = database_value
    local_value += 1
    time.sleep(1)
    database_value = local_value

  #lock.release()


if __name__ == "__main__":
  print(f'Value before threading: {database_value}')

  lock = Lock()

  thread1 = Thread(target=increase, args=(lock,))
  thread2 = Thread(target=increase, args=(lock,))

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print(f'Value after threading: {database_value}')

  print('End of threading')



