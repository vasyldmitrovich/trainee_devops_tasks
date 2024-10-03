import unittest
import os
import logging
from my_app.app import process_data, setup_logging


class TestApp(unittest.TestCase):
    def setUp(self):
        self.log_file = 'test_log.txt'
        setup_logging(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_process_data(self):
        self.assertEqual(process_data("hello"), "HELLO")

    def test_logging(self):
        process_data("test")
        with open(self.log_file, 'r') as f:
            logs = f.read()
        self.assertIn("Processing data: test", logs)


if __name__ == '__main__':
    unittest.main()

# PASS 65 COVERAGE --- FOR BAD CASE EXAMPLE
# import unittest
# from my_app.app import process_data
#
# class TestApp(unittest.TestCase):
#     def test_process_data(self):
#         self.assertEqual(process_data("hello"), "HELLO")
#
# if __name__ == '__main__':
#     unittest.main()
