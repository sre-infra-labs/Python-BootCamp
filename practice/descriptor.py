class Identity:
    def __init__(self, val):
        self.num = val
    def __get__(self, obj, type=None):
        return self.num
    def __set__(self, obj, value):
        if(value > 0):
            self.num = value
        else:
            raise ValueError("negative value")

class Product:
    id = Identity(12)

item = Product()
print(item.id)
#item.id = -45

class Person:
    @property
    def name(self):
        return self.person_name
    
    @name.setter
    def name(self, name):
        self.person_name = name
    
person = Person()
person.name = "Krishna"
print(person.name)
print(person.person_name)