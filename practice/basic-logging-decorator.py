def multiply(first, second):
    return first * second

def loggable(target):
    def capability(*args, **kwargs):
        print(args)
        result = target(*args)
        print(result)
        return result
    return capability

#print(multiply(10, 5))

product_of = loggable(multiply)
print(product_of(10, 5))
