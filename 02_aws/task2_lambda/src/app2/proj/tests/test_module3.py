import unittest
import module3

class TestModule3(unittest.TestCase):

    def test_fetch_status_code(self):
        self.assertEqual(module3.fetch_status_code("https://www.google.com"), 200)
        self.assertIsNone(module3.fetch_status_code("https://www.invalidurl.com"))

    def test_is_url_accessible(self):
        self.assertTrue(module3.is_url_accessible("https://www.google.com"))
        self.assertFalse(module3.is_url_accessible("https://www.invalidurl.com"))

    def test_count_valid_urls(self):
        urls = ["https://www.google.com", "https://www.github.com", "https://www.invalidurl.com"]
        self.assertEqual(module3.count_valid_urls(urls), 2)

    def test_get_invalid_urls(self):
        urls = ["https://www.google.com", "https://www.github.com", "https://www.invalidurl.com"]
        self.assertEqual(module3.get_invalid_urls(urls), ["https://www.invalidurl.com"])

if __name__ == '__main__':
    unittest.main()
