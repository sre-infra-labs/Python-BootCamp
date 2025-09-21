from utils.generators import getId
from services.repository import InMemoryRepository
from services.exceptions import EmployeeNotFoundException

class EmployeeDirectory:
    def __init__(self):
        self.repo = InMemoryRepository()
        self.eid = getId()

    def add(self, employee):
        """Adds the specified employee to the directory and returns the id"""

        employee["id"] = next(self.eid)
        self.repo.add(employee)
        return employee["id"]

    def remove_by(self, id):
        """Removes the employee with the specified id"""

        self.repo.remove_by(id)

    def find_by(self, id):
        """Finds an employee by the specified id"""

        emp = self.repo.find_by(id)
        if(emp == None):
            raise EmployeeNotFoundException(" not found")
        return emp

    def search_by(self, name):
        """Searches all employees with the specified name"""

        return [v for k, v in self.repo.list().items() if v["name"] == name]

    def filter_by(self, condition): 
        """Searches all employees for the given condition"""

        return [v for k, v in self.repo.list().items() if condition(v)]

    def count(self):
        """Returns the number of employees in the directory"""

        return len(self.repo.list())

    def list(self):
        """Returns the complete list of employees"""

        return self.repo.list()