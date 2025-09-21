from decorators.loggable import loggable
from decorators.validatable import validatable

class EmployeeDirectory:
    def __init__(self):
        self.directory = {}
        self.eid = 0

    @loggable
    @validatable
    def add(self, employee):
        """Adds the specified employee to the directory and returns the id"""
        self.eid += 1
        employee["id"] = self.eid
        self.directory[self.eid] = employee
        return self.eid

    def remove_by(self, id):
        """Removes the employee with the specified id"""

        del self.directory[id]

    def find_by(self, id):
        """Finds an employee by the specified id"""

        return self.directory[id]

    def search_by(self, name):
        """Searches all employees with the specified name"""

        return [v for k, v in self.directory.items() if v["name"] == name]

    def filter_by(self, condition): 
        """Searches all employees for the given condition"""

        return [v for k, v in self.directory.items() if condition(v)]

    def count(self):
        """Returns the number of employees in the directory"""

        return len(self.directory)

    def list(self):
        """Returns the complete list of employees"""

        return self.directory.items()