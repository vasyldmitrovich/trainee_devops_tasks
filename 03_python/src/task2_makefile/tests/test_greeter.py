# tests/test_greeter.py
import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_say_hello(self):
        greet = Greeter()
        self.assertEqual(greet.say_hello("John"), "Hello, John!")

    def test_say_goodbye(self):
        greet = Greeter()
        self.assertEqual(greet.say_goodbye("John"), "Goodbye, John!")

if __name__ == '__main__':
    unittest.main()
