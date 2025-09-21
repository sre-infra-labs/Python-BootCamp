def loggable(target):
    def capability(*args, **kwargs):
        print(args)
        result = target(*args)
        print(result)
        return result
    return capability

def validatable(*rules):
    def decorate(target):
        def capability(*args, **kwargs):
            for index, arg in enumerate(args):
                if rules[index](arg) == False:
                    print(arg, " is invalid value for argument ", index+1)
                    return
            return target(*args)
        return capability
    return decorate

@loggable
@validatable(lambda a:a>0, lambda a:a>0, lambda a:a>0)
def interest(p, t, r):
    return p * t * r / 100

def multiply(first, second):
    return first * second

product_of = loggable(validatable(lambda p:type(p)==int, lambda p:p>0)(multiply))

print(interest(100, 3, -2))
print(product_of("ten", 5))