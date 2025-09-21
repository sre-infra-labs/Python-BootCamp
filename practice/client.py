import glarimy.services.directory as dir

if __name__ == "__main__":
    add, remove_by, find_by, search_by, count, list, filter_by, count_by, map_by = dir.directory()
    krishna = add({"name":"Krishna", "phone": 9731423161})
    mohan = add({"name":"Mohan", "phone": 9731423162})
    koyya = add({"name":"Koyya", "phone": 9731423163})
    print(filter_by(lambda e: e["id"] < 1002))
    print(count_by(lambda e: e["phone"] == 9731423161))
    print(map_by(lambda e: "+91-" + str(e["phone"])))






