"""
Unit tests for the calculator library12
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(2, 6)
        self.assertEqual(result, 8)
        

    def test_subtraction(self):
        result = calculator.subtract(4,1)
        self.assertEqual(result, 3)
        
        
if __name__ == '__main__':
    unittest.main()
