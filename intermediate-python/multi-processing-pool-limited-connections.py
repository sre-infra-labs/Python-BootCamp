import multiprocessing
from multiprocessing import Pool, current_process
import time
import itertools

TOTAL_PROCESSES = 4
_worker_counter = itertools.count(1)   # global counter for workers

def init_worker():
    """
    Runs once inside each worker and sets a unique name.
    """
    index = next(_worker_counter)
    name = f"multi-ps-{index}-of-{TOTAL_PROCESSES}"
    current_process().name = name
    print(f"[INIT] Started worker: {name}")

def square(x):
    print(f"[{current_process().name}] computing square({x})")
    time.sleep(1)
    return x * x

if __name__ == "__main__":
    with Pool(
        processes=TOTAL_PROCESSES,
        initializer=init_worker
    ) as pool:
        results = pool.map(square, range(20))
        print(results)
