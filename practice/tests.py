import unittest

def add(first, second): return first + second

def decorate(target):
    def feature(*args):
        for arg in args:
            if arg < 0:
                raise ValueError
        return target(*args)
    return feature

class TestFunctions(unittest.TestCase):
        def test_add_with_positives(self):
            self.assertTrue(add(1,2) == 3)
        
        def testDecorator(self):
            with self.assertRaises(ValueError):
                decorate(add)(1, -3)

unittest.main()