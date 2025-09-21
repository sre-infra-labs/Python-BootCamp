from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def add(self, entry):
        pass
    
    @abstractmethod
    def list(self):
        pass    
    
    @abstractmethod
    def remove_by(self, id):
        pass
    
    @abstractmethod
    def find_by(self, id):
        pass

class InMemoryRepository(IRepository):
    def __init__(self):
        self.entries = {}

    def add(self, entry):
        self.entries[entry["id"]] = entry
    
    def list(self):
        return self.entries.items()
    
    def remove_by(self, id):
        del self.entries[id]
    
    def find_by(self, id):
        return self.entries[id]