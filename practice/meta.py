drivers = {}

class DriverMetaClass(type):
    def __new__(claz, name, bases, attrs):
        drivers[attrs["url"]] = cls = type.__new__(claz, name, bases, attrs)
        return cls

class Driver(object, metaclass=DriverMetaClass):
    url = "generic"

    def connect(self):
        print("connecting to generic")

class MySqlDriver(Driver):
    url = "mysql"
    def connect(self):
        print("connecting to mysql")

class OracleDriver(Driver):
    url = "oracle"
    def connect(self):
        print("connecting to oracle")

db = input("What your database? [generic/mysql/oracle]: ")
driver = drivers[db]()
driver.connect()