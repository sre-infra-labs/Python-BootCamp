# https://bitbucket.org/glarimy/glarimy-py/src/master/
import directory_register as register

def emp_directory():
    """
    [summary]

    Raises:
        ValueError: [description]
        Exception: [description]
        ValueError: [description]
        ValueError: [description]
        Exception: [description]

    Returns:
        [type]: [description]
    """
    # Initialize register
    directory = {}
    reg = register.directory_register() # open employee register

    def add(employee):
        """
        Adds the specified employee to the directory and returns the id

        Parameters: employee - a dictionary with valid name, email and phone
        Returns: eid - newly generated employee id
        Raises: ValueError - if employee is invalid
        """

        if(employee == None):
            raise ValueError

        #global eid
        eid = next(reg)
        employee["id"] = eid
        directory[eid] = employee
        return eid

    def find_by(id):
        """
        Finds an employee by the specified id

        Parameters: id - an integer
        Returns: employee - employee with the specified id, if found
        Raises: Exception - if employee with the specified id is not found
        """
        
        employee = directory[id]
        if (employee == None):
            raise Exception

        return employee

    def find_by_name(name):
        """Finds an employee by the specified name

        Parameters: name - a string
        Returns: employee - employee with the specified name, if found
        Raises: Exception - if employee with the specified name is not found
        """
        if (name == None):
            raise ValueError
        if (name.strip() == None or len(name.strip()) == 0):
            raise ValueError

        for emp in directory.values():
            if emp['name'] == name:
                return emp
        else:
            raise Exception("Employee not found")

    return add, find_by, find_by_name


if __name__ == "__main__":

    try:
        add, find_by, find_by_name = emp_directory()
        print(f"\nAdd an employee")
        empid1 = add({"name": "Krishna", "email": "krishna@glarimy.com", "phone": 9731423166})
        print(f"New employee [{empid1}] added")

        print (f"\nFind by id ({id}) => ")
        print (find_by(empid1))

        print(f"\nAdd another employee")
        empid2 = add({"name": "Ajay", "email": "ajay.dwivedi@gmail.com", "phone": 9650111854})
        print(f"New employee [{empid2}] added")

        name = 'Krishna'
        print (f"\nFind by name ({name}) => ")
        print (find_by_name(name))
    except ValueError:
        print ("ValueError: Invalid employee data")
    except Exception:
        print ("Exception: Employee not found")