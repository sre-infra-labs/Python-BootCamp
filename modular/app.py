import services.directory as directory

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