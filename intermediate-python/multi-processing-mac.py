from multiprocessing import Process
import os
import time

def multiply_number(i):
    for n in range(100):
        i*n
        time.sleep(0.5)

if __name__ == '__main__':
    processes = []
    num_cpu = os.cpu_count()

    print(f'Number of CPU cores: {num_cpu}')
    for i in range(num_cpu):
        p = Process(target=multiply_number, args=(i,))
        processes.append(p)

    print(f'Created {len(processes)} processes.')

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('End Main')
