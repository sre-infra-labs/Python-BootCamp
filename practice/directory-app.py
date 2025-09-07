import packages.directory as directory

id = directory.add({"name": "Krishna", "email": "krishna@glarimy.com", "phone": 9731423166})

print ("Find by id => ")
print (directory.find_by(id))

print ("Find by name => ")
print (directory.find_by_name('Krishna'))

