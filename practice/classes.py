from abc import ABC, abstractmethod

class AbstractStack(ABC):
    __slots__ = ['entries']

    def __init__(self):
        self.entries = []

    @abstractmethod
    def push(self, entry):
        self.entries.append(entry)

    @abstractmethod
    def pop(self):
        return self.entries.pop()

class UnlimitedStack(AbstractStack):
    __slots__ = ['entries']

    def push(self, entry):
        super().push(entry)

    def pop(self):
        return super().pop()
    
class LimitedStack(AbstractStack):
    __slots__ = ['entries', 'size', 'index']
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size
        self.entries = []
        self.index = 0

    def push(self, entry):
        if self.index < self.size:
            self.entries.append(entry)
            self.index += 1
        else:
            raise IndexError("Out of bounds")
    
    def pop(self):
        if self.index < 0:
            raise IndexError("Out of bounds")
        
        self.index -= 1
        return self.entries.pop()

stack = LimitedStack()
#stack = UnlimitedStack()
#stack.attr = "value"

for i in range(25):
    try:
        stack.push(i)
    except IndexError:
        print("stack over flow")
        break
    
while True:
    try:
        print(stack.pop(), end=" ")
    except IndexError:
        print()
        print("stack under flow")
        break
