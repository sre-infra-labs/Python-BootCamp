from dataclasses import dataclass

@dataclass
class Person:
    name:str
    phone:int

me = Person("Krishna", 1234)
print(me)