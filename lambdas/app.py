from services.directory import directory

if __name__ == "__main__":
    add, find_by, search_by, count, list, remove_by, filter_by = directory()
    
    add({"name":"Krishna", "phone": 1234})
    add({"name":"Mohan", "phone": 2345})
    add({"name":"Koyya", "phone": 3456})

    print(filter_by(lambda e: e["name"].startswith("K")))