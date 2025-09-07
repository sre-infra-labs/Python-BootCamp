# Python-BootCamp
This repository contains practice files for Python

**MyBinder** - Online Python Practice Page
https://mybinder.org/v2/gh/imajaydwivedi/Python-BootCamp/3dfb1137bd6b0603b089ffaa6626b09ad790ed5c

**MyBinder** - Link to share with Others
https://mybinder.org/v2/gh/imajaydwivedi/Python-BootCamp/HEAD

# Python 3.7

## References
1. [Python Official Documentation](https://docs.python.org/3.7/tutorial/index.html)

## Setup
- Download python from [https://www.python.org/downloads/release/python-375/](https://www.python.org/downloads/release/python-375/)
- Install
- Verify with shell
```
~/workspace/python3
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
- Come out of the shell by `CTRL+D`
- Write a script `~/workspace/hello.py`
```Python
name = input("Enter your name: ")
print("Welcome, ", name, "!")
```
- Run the script 
```
[~/workspace]$ python3 hello.py
```

## Illustrations
### Functions, Dictionaries, Lists, Comprehensions
*Implement a solution for employee directory in `directory.py` using functions to add an employee, remove an employee by id, find an employee by id, search employees by name and list all employees. The employee data includes id, name and phone number. The employee is id to be generated and returned by the system as part of add functionality.*

~/workspace/directory.py

```Python

directory = {}
id = 0

def add(employee):
    """Adds the specified employee to the directory and returns the id"""
    global id
    id += 1
    employee["id"] = id
    directory[id] = employee
    return id

def remove_by(id):
    """Removes the employee with the specified id"""

    del directory[id]

def find_by(id):
    """Finds an employee by the specified id"""

    return directory[id]

def search_by(name):
    """Searches all employees with the specified name"""

    employees = []
    [employees.append(v) for k, v in directory.items() if v["name"] == name]

    return employees

def count():
    """Returns the number of employees in the directory"""

    return len(directory)

def list():
    """Returns the complete list of employees"""

    return directory.items()

if __name__ == "__main__":
    add({"name":"Krishna", "phone": 1234})
    add({"name":"Mohan", "phone": 2345})
    add({"name":"Koyya", "phone": 3456})
    print(list())
    print(count())
    print(find_by(1))
    print(search_by("Koyya"))
    remove_by(1)
    print(list())
```

```
[~/workspace]$ python3 directory.py`
```

### Modules and Packages
*Separate the employee directory (`directory.py`) in to a package named `glarimy.services` and import it into `client.py``*

```
export PYTHONPATH=~/workspace/
```

~/workspace/glarimy/services/directory.py

```Python
directory = {}
id = 0

def add(employee):
    """Adds the specified employee to the directory and returns the id"""
    global id
    id += 1
    employee["id"] = id
    directory[id] = employee
    return id

def remove_by(id):
    """Removes the employee with the specified id"""

    del directory[id]

def find_by(id):
    """Finds an employee by the specified id"""

    return directory[id]

def search_by(name):
    """Searches all employees with the specified name"""

    employees = []
    [employees.append(v) for k, v in directory.items() if v["name"] == name]

    return employees

def count():
    """Returns the number of employees in the directory"""

    return len(directory)

def list():
    """Returns the complete list of employees"""

    return directory.items()
```

~/workspace/client.py

```Python
import glarimy.services.directory as directory

if __name__ == "__main__":
    directory.add({"name":"Krishna", "phone": 1234})
    directory.add({"name":"Mohan", "phone": 2345})
    directory.add({"name":"Koyya", "phone": 3456})
    print(directory.list())
    print(directory.count())
    print(directory.find_by(1))
    print(directory.search_by("Koyya"))
    directory.remove_by(1)
    print(directory.list())
```

```
[~/workspace]$ python3 client.py`
```

### Generators
*Develop a generator to generate employee-id infinitely in module `generators.py` under `glarimy.utils` package and use it in the `directory.py`*

~/workspace/glarimy/utils/generators.py

```Python
def id():
    """Generates a unique id starting from 1001, in sequence """
    
    id = 1000
    while True:
        id += 1
        yield id
```

~/workspace/glarimy/services/directory.py

```Python
import glarimy.utils.generators as generators

directory = {}
eid = generators.id()

def add(employee):
    """Adds the specified employee to the directory and returns the id"""
    
    id = next(eid)
    employee["id"] = id
    directory[id] = employee
    return id

def remove_by(id):
    """Removes the employee with the specified id"""

    del directory[id]

def find_by(id):
    """Finds an employee by the specified id"""

    return directory[id]

def search_by(name):
    """Searches all employees with the specified name"""

    employees = []
    [employees.append(v) for k, v in directory.items() if v["name"] == name]

    return employees

def count():
    """Returns the number of employees in the directory"""

    return len(directory)

def list():
    """Returns the complete list of employees"""

    return directory.items()
```

~/workspace/client.py

```Python
import glarimy.services.directory as directory

if __name__ == "__main__":
    directory.add({"name":"Krishna", "phone": 1234})
    directory.add({"name":"Mohan", "phone": 2345})
    directory.add({"name":"Koyya", "phone": 3456})
    print(directory.list())
    print(directory.count())
    print(directory.find_by(1))
    print(directory.search_by("Koyya"))
    directory.remove_by(1)
    print(directory.list())
```
### Lambda
*Add functionality to filter employees, to count employees and to map the employees, based on user defined criteria, in the directory.py*

~/workspace/glarimy/utils/generators.py
```Python
def id():
    """Generates a unique id starting from 1001, in sequence """
    
    id = 1000
    while True:
        id += 1
        yield id
```

~/workspace/glarimy/services/directory.py
```Python
import glarimy.utils.generators as generators

directory = {}
eid = generators.id()

def add(employee):
    """Adds the specified employee to the directory and returns the id"""
    
    id = next(eid)
    employee["id"] = id
    directory[id] = employee
    return id

def remove_by(id):
    """Removes the employee with the specified id"""

    del directory[id]

def find_by(id):
    """Finds an employee by the specified id"""

    return directory[id]

def search_by(name):
    """Searches all employees with the specified name"""

    employees = []
    [employees.append(v) for k, v in directory.items() if v["name"] == name]

    return employees

def count_by(criteria):
    """Retruns the count of employees matching the criteria"""

    return len([v for k, v in directory.items() if criteria(v)==True])

def map_by(criteria):
    """Returns only an object for every employee, where the object created based on the criteria"""

    return [criteria(v) for k, v in directory.items()]

def filter_by(criteria):
    """Filters all the employees based on the supplied criteria and returns

    The criteria must take employee as the input    
    The criteria must return a boolean
    """

    employees = []
    [employees.append(v) for k, v in directory.items() if criteria(v) == True]

    return employees

def count():
    """Returns the number of employees in the directory"""

    return len(directory)

def list():
    """Returns the complete list of employees"""

    return directory.items()
```

~/workspace/client.py
```Python
import glarimy.services.directory as directory

if __name__ == "__main__":
    krishna = directory.add({"name":"Krishna", "phone": 9731423161})
    mohan = directory.add({"name":"Mohan", "phone": 9731423162})
    koyya = directory.add({"name":"Koyya", "phone": 9731423163})
    print(directory.filter_by(lambda e: e["id"] < 1002))
    print(directory.count_by(lambda e: e["phone"] == 9731423161))
    print(directory.map_by(lambda e: "+91-" + str(e["phone"])))
```

## Assignments

4. [The first casestudy](glarimy-py-case-01.py) exports employee data into XML and JSON formats. Refactor it for the following:

  * Follow naming conventions
  * Use docstrings
  * Follow indentation 
  * Apply factory pattern
  * Achieve zero code changes on the client to support other new formats