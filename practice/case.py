#0. Have IDirectory abstract base (add->, filter->[])
#1. Have a Directory implementation of employees (async)
#2. Have a Storage to store employees (no biz logic)(async)
#3. Employee (name, phone) + eid (generator)
#4. Have a strategy to handle multiple Directory implements

#comprehensions
#base->derived
#abstract 
#async/await
#generators
#dataclasses
#functors

import asyncio 
import time
from dataclasses import dataclass
from abc import ABC, abstractmethod

def id():
    id = 1000
    while True:
        id += 1
        yield id

@dataclass
class Employee():
    name: str
    phone: int
    eid: int 

class AbstractDirectory(ABC):
    @abstractmethod
    async def add(self, employee): pass 

    @abstractmethod
    async def filter_by(self, crieteria):pass

class Storage():
    entries = {}

    async def insert(self, k, v):
        await asyncio.sleep(1)
        Storage.entries[k] = v

    async def list(self):
        await asyncio.sleep(1)
        return Storage.entries.items()

class Directory(AbstractDirectory):
    __slots__ = ['storage', 'generator']

    def __init__(self):
        self.storage = Storage()
        self.generator = id()
    
    async def add(self, employee):
        id = next(self.generator)
        employee.id = id
        await self.storage.insert(id, employee)
        return

    async def filter_by(self, crieteria):
        employees = []
        items = await self.storage.list()
        [employees.append(v) for k, v in items if crieteria(v) == True]
        return employees

async def main():
    dir = Directory()
    await dir.add(Employee("Krishna", 1234, 0))
    list = await dir.filter_by(lambda e: e.phone < 0)
    print(list)

asyncio.run(main())
