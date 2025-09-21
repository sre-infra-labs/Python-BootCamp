class Repository():
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

repo1 = Repository()
repo2 = Repository()
repo3 = StableRepository()
repo1.add(1)
repo1.add(2)
repo2.add(3)
repo3.add(4)
repo2.add(None)
repo3.add(None)
print(repo1.list())
print(repo1.entries)
print(repo1.all())
print(Repository.repo)
print(repo2.list())
#print(repo3.list())