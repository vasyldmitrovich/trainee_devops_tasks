import unittest
from task3_project import module2

class TestModule2(unittest.TestCase):

    def test_square(self):
        self.assertEqual(module2.square(2), 4)

    def test_cube(self):
        self.assertEqual(module2.cube(3), 27)

    def test_square_root(self):
        self.assertEqual(module2.square_root(9), 3)
        self.assertIsNone(module2.square_root(-1))

    def test_cube_root(self):
        self.assertAlmostEqual(module2.cube_root(27), 3)

if __name__ == '__main__':
    unittest.main()
