import glarimy.utils.generators as generators

def directory():
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
    
    return add, remove_by, find_by, search_by, count, list, filter_by, count_by, map_by