def getId():
    """Generates a unique id starting from 1001, in sequence """
    
    id = 1000
    while True:
        id += 1
        yield id