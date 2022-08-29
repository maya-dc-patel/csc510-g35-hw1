import sys
sys.path.insert(1, 'code')
import calculator
import unittest

class TestCalculator(unittest.TestCase):
    def testDivide(self):
        """
        Test if function divide works
        """
        a = 6
        b = 3
        result = calculator.divide(a,b)
        self.assertEqual(result, 2)

    def testAddition(self):
        """
        Test if function addition works
        """
        a = 6
        b = 3
        result = calculator.addition(a,b)
        self.assertEqual(result, 9)

    def testSubtraction(self):
        """
        Test if function subtraction works
        """
        a = 6
        b = 3
        result = calculator.subtraction(a,b)
        self.assertEqual(result, 3)

    def testMultiplication(self):
        """
        Test if function multiplication works
        """
        a = 6
        b = 3
        result = calculator.multiplication(a,b)
        self.assertEqual(result, 18)

if __name__ == '__main__':
    unittest.main()