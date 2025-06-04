from multiprocessing import Pool
# https://superfastpython.com/multiprocessing-pool-map/

def cube(number):
  return number*number*number

if __name__ == "__main__":
  numbers = range(10)

  pool = Pool()

  # map, apply, join, close

  # run multiple scripts
  result = pool.map(cube,numbers)

  '''
  # need to run single script
  result = pool.apply(cube,(numbers[3],))
  '''

  pool.close()
  pool.join()

  print(type(result))
  print(result)

  print('End main')

