class DirectoryException(Exception):
    def __init__(self, message):
        self.message = message

class EmployeeNotFoundException(DirectoryException):
    def __init__(self, message):
        super(message)