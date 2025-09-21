class Repository(object):
    repo = []
    __slots__ = ['entries']
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

repo1 = Repository()
repo1.name = "First Repo"