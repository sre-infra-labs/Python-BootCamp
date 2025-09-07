import logging
import traceback

try:
    #a = 5 / 0
    #b = a + '10'
    c = [1,2,3,4,5]
    print(c[6])
except ZeroDivisionError as e:
    print(f"ZeroDivisionError occurred. \n{e}")
except TypeError as e:
    print(f"TypeError occurred. \n{e}")
except Exception as e:
    exception_name = type(e).__name__
    print(f"Exception [{exception_name}] occurred. \n{e}")
    print(traceback.format_exc())
else:
    print('everything is fine')
finally:
    print('cleanup things.')