def directory():
    directory = {}
    eid = 0

    def add(employee):
        """Adds the specified employee to the directory and returns the id"""
        nonlocal eid
        eid += 1
        employee["id"] = eid
        directory[eid] = employee
        return eid

    def remove_by(id):
        """Removes the employee with the specified id"""

        del directory[id]

    def find_by(id):
        """Finds an employee by the specified id"""

        return directory[id]

    def search_by(name):
        """Searches all employees with the specified name"""

        return [v for k, v in directory.items() if v["name"] == name]

    def count():
        """Returns the number of employees in the directory"""

        return len(directory)

    def list():
        """Returns the complete list of employees"""

        return directory.items()

    return add, find_by, search_by, count, list, remove_by