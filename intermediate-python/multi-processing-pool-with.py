from multiprocessing import Pool
# https://superfastpython.com/multiprocessing-pool-map/

def cube(number):
  return number*number*number

if __name__ == "__main__":
  numbers = range(30)

  # run multiple scripts
  with Pool() as pool:
    # execute tasks in order
    # for result in pool.map(cube,numbers):
    #   print(f'Got result: {result}', flush=True)
    result = pool.map(cube,numbers)

    pool.close()
    pool.join()
  # process pool is closed automatically

  print(f'Result: {result}')
  print('End main')

