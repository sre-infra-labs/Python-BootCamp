class InvalidEntryError(Exception):
    def __init__(self, message, entry):
        self.message = message
        self.entry = entry

class Repository():
    def __init__(self):
        self.entries = []
    def add(self, entry):
        if entry == None:
            raise InvalidEntryError("entry is invalid", entry)
        self.entries.append(entry)
    def list(self):
        return self.entries

repo = Repository()
try:
    repo.add(1)
    repo.add(2)
    repo.add(3)
    #repo.add(None)
except InvalidEntryError as iee:
    print('failed to add', iee.args[1])
else:
    print('all added successfully')
finally:
    print(repo.list())