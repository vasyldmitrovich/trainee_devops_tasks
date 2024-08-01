import unittest
from app import app

class TestProductsAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        response = self.app.post('/api/products', data={'name': 'Test Product', 'price': 10.0})
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        response = self.app.get('/api/products/1')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        response = self.app.patch('/api/products/1', data={'name': 'Updated Product', 'price': 15.0})
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = self.app.delete('/api/products/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
