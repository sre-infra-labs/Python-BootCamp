# In serializer_demo.py

import json
import xml.etree.ElementTree as et

class employee:
    def __init__(self, EID, name, email):
        self.EID = EID
        self.name = name
        self.email = email

class exporter:
    def Export(self, employee, format):
        if format == 'json':
            emp = {
                'eid': employee.EID,
                'name': employee.name,
                'email': employee.email
            }
            return json.dumps(emp)
        elif format == 'xml':
            emp = et.Element('emp', attrib={'eid': employee.EID})
            name = et.SubElement(emp, 'name')
            name.text = employee.name
            email = et.SubElement(emp, 'email')
            email.text = employee.email
            return et.tostring(emp, encoding='unicode')
        else:
            raise ValueError(format)

if __name__ == "__main__":
        exporter = exporter()
        while True:
            print ("Choose json/xml/exit: ", end=" ")
            option = input()

            if option == "exit":
                break

            str = exporter.Export(employee("1", 'Krishna', 'krishna@glarimy.com'), option)
            print (str)
