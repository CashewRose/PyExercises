import unittest
from Calc import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    global C
    
    C = Calculator()
    
    
    def test_add(self):


        self.assertEqual(C.add(2, 7), 9)
        self.assertEqual(C.add(2, 7.5), 9.5)
        self.assertEqual(C.add(-2, 7), 5)


    def test_subtract(self):

        self.assertEqual(C.subtract(7, 2), 5)
        self.assertEqual(C.subtract(7.5, 2), 5.5)
        self.assertEqual(C.subtract(-7, 2), -9)

  # Write test methods for subtract, multiply, and divide
    def test_multiply(self):

        self.assertEqual(C.multiply(2, 2), 4)
        self.assertEqual(C.multiply(2, 2.5), 5)
        self.assertEqual(C.multiply(-2, 2.5), -5)


    def test_divide(self):

        self.assertEqual(C.divide(4, 2), 2)
        self.assertEqual(C.divide(4.5, 2), 2.25)
        self.assertEqual(C.divide(-4.5, 2), -2.25)

if __name__ == '__main__':
    unittest.main()