directory = {}
eid = 0

def add(employee):
    """
    Adds the specified employee to the directory and returns the id
    
    Parameters: employee - a dictionary with valid name, email and phone
    Returns: eid - newly generated employee id
    Raises: ValueError - if employee is invalid
    """

    if(employee == None):
        raise ValueError

    global eid 
    eid += 1
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

if __name__ == "__main__":

    try:    
        id = add({"name": "Krishna", "email": "krishna@glarimy.com", "phone": 9731423166})
        print (find_by(3))
    except ValueError: 
        print ("Invalid employee data")
    except Exception:
        print ("Employee not found")