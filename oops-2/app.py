from services.directory import EmployeeDirectory
from services.exceptions import EmployeeNotFoundException

if __name__ == "__main__":
    directory = EmployeeDirectory()
    directory.add({"name":"Krishna", "phone": 1234})
    print(directory.list())
    try:
        print(directory.find_by(1002))
    except EmployeeNotFoundException as e:
        print(e)