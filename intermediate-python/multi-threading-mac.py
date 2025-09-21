from threading import Thread
import os
import time

def multiply_number(i):
    for n in range(100):
        i*n
        time.sleep(0.5)

if __name__ == '__main__':
    threads = []
    num_cpu = os.cpu_count()

    print(f'Number of CPU cores: {num_cpu}')
    for i in range(num_cpu*2):
        p = Thread(target=multiply_number, args=(i,))
        threads.append(p)

    print(f'Created {len(threads)} threads.')

    for p in threads:
        p.start()

    for p in threads:
        p.join()

    print('End Main')
