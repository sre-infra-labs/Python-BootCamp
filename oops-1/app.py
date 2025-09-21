from services.directory import EmployeeDirectory
if __name__ == "__main__":
    directory = EmployeeDirectory()
    directory.add({"name":"Krishna", "phone": 1234})
    directory.add(None)
    print(directory.list())