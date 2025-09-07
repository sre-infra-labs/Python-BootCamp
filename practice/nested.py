def next_counter(count):
    def increment():
        nonlocal count
        count += 1
        return count

    return increment()

print(next_counter(5))
print(next_counter(45))
