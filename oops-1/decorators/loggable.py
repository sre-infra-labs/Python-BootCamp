def loggable(target):
    def capability(*args, **kwargs):
        print(args)
        result = target(*args)
        return result
    return capability