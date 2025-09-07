def validatable(*rules):
    def decorate(target):
        def capability(*args, **kwargs):
            if(rules[0](args[0]) == False):
                print(args[0], " is invalid value for argument 0")
                return
            return target(*args)
        return capability
    return decorate