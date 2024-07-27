import unittest
from unittest.mock import patch
import AppLogV1
import logging

class TestAppLogV1(unittest.TestCase):
    @patch('AppLobV1.logging')
    def test_square_number(self, mock_logging):
        # Test valid numbers
        self.assertEqual(AppLogV1.square_number(5), 25)
        self.assertEqual(AppLogV1.square_number(10), 100)
        self.assertEqual(AppLogV1.square_number(15), 225)

    @patch('AppLogV1.logging')
    def test_logging_info(self, mock_logging):
        # Test logging for valid numbers
        with patch('builtins.print'):
            AppLogV1.square_number(5)
            AppLogV1.square_number(10)
            AppLogV1.square_number(15)

        self.assertTrue(mock_logging.info.called)
        self.assertTrue(mock_logging.info.call_count == 4)  # Including the request version log

    @patch('AppLogV1.logging')
    def test_logging_error(self, mock_logging):
        # Test logging for an invalid input
        with patch('builtins.print'):
            AppLogV1.square_number('err')

        self.assertTrue(mock_logging.error.called)
        self.assertIn('Error in calculation for', mock_logging.error.call_args[0][0])

if __name__ == '__main__':
    unittest.main()
