import unittest
from task3_project import module1

class TestModule1(unittest.TestCase):

    def test_add(self):
        self.assertEqual(module1.add(1, 2), 3)
        self.assertEqual(module1.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(module1.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(module1.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(module1.divide(10, 2), 5)
        self.assertIsNone(module1.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
