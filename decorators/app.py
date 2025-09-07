from services.directory import directory

def loggable(target):
    def capability(*args, **kwargs):
        print(args)
        result = target(*args)
        return result
    return capability

def validatable(*rules):
    def decorate(target):
        def capability(*args, **kwargs):
            if(rules[0](args[0]) == False):
                print(args[0], " is invalid value for argument 0")
                return
            return target(*args)
        return capability
    return decorate

if __name__ == "__main__":
    add, find_by, search_by, count, list, remove_by, filter_by = directory()
    add_with_logging = loggable(add)
    add_with_validation = (validatable(lambda e: e != None))(add_with_logging)
    add_with_validation({"name":"Krishna", "phone": 1234})
    add_with_validation(None)