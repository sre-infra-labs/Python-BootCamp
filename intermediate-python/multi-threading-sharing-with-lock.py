from threading import Thread, Lock
import time

database_value = 0

def increment(lock):
    global database_value

    with lock:
        local_value = database_value
        # do some work
        time.sleep(1)
        database_value = local_value + 1

if __name__ == "__main__":
    print(f'start database_value = {database_value}')

    lock = Lock()

    thread1 = Thread(target=increment, args=(lock,))
    thread2 = Thread(target=increment, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'end database_value = {database_value}')

    print(f'End of logic.')