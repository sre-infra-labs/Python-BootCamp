def get_computes(first, second):
    def add():
        return first+second
    def multiply():
        return first*second
        
    return add, multiply

add, multiply = get_computes(10, 34)

print("sum: ", add())
print("product: ", multiply())