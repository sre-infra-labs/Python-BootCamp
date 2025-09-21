from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def add(self, entry):
        pass

class Repository(IRepository):
    repo = []
    def __init__(self):
        self.entries = []
    def add(self, entry):
        self.entries.append(entry)
        Repository.repo.append(entry)
    def list(self):
        return self.entries
    def all(self):
        return Repository.repo

class StableRepository(Repository):
    def add(self, entry):
        if(entry != None):
            super().add(entry)

repo = Repository()