import unittest
import packages.directory as arcdir

# Initiate directory
id = arcdir.add({"name": "Krishna", "email": "krishna@glarimy.com", "phone": 9731423166})

class TestFunctions(unittest.TestCase):

        def test_find_by_id_existing(self):
            self.assertTrue(arcdir.find_by(1) != None)

        def test_find_by_id_nonexisting(self):
            with self.assertRaises(Exception):
                self.assertTrue(arcdir.find_by(10) != None)

        def test_find_by_name_invalid_parameter_value(self):
            with self.assertRaises(ValueError):
                self.assertTrue(arcdir.find_by_name(' '))

unittest.main()