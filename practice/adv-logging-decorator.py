def loggable(target):
    def capability(*args, **kwargs):
        print(args)
        result = target(*args)
        print(result)
        return result
    return capability

@loggable
def interest(p, t, r):
    return p * t * r / 100

print(interest(100, 3, -2))