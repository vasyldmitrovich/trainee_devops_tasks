# tests/test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(5, 10), 15)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 5), 5)

if __name__ == '__main__':
    unittest.main()
