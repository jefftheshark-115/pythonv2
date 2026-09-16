import unittest

class TestMain(unittest.TestCase):
    
    def test_values(self):
        a = 'Vilnius'
        b = ['vilnius','riga','tallinn']
        self.assertIn(a, b)  # assert test needed

if __name__ == '__main__':
    unittest.main()  