import unittest
import packages.library as lib

# Initialize library
lib.add_book({'isbn':'20200312-01','title':'Clean code for python','pages':200, 'author':'Krishna'})
lib.add_book({'isbn':'20210312-02','title':'SQL Server on Linux','pages':432, 'author':'Bob Ward'})
lib.add_book({'isbn':'20050312-01','title':'TSQL Fundamentals','pages':280, 'author':'It-Zik-Ben-Gen'})
lib.add_book({'isbn':'20190312-03','title':'Pro SQL Server Internals','pages':900, 'author':'Dmitri'})

class TestFunctions(unittest.TestCase):

    def test_add_book_valid_entry(self):
        self.assertTrue(lib.add_book({'isbn':'20190312-04','title':'SQL Server Querying','pages':430, 'author':'It-Zik-Ben-Gen'}) != None)

    def test_add_book_invalid_entry(self):
        with self.assertRaises(ValueError):
            self.assertTrue(lib.add_book('Something'))

    def test_add_book_duplicate(self):
        with self.assertRaises(Exception):
            self.assertTrue(lib.add_book({'isbn':'20190312-04','title':'SQL Server Querying','pages':430, 'author':'It-Zik-Ben-Gen'}) != None)


unittest.main()