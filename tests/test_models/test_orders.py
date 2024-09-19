#!/usr/bin/python3
"""
Test_Order
    All the tests for the Order model are implemented here.
"""

import unittest
from models.orders import Order
from models.products import Product
from models.users import User
import pep8
from models import storage

class TestOrder(unittest.TestCase):
    """Tests for the Order model."""
    def setUp(self):
        """Set up a fresh instance before each test."""
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            user_password="password123",
            role="professor"
        )
        self.product = Product(
            name="Sample Product",
            ref="newref",
            description="This is a sample product description.",
            quentity=10
        )
        self.order = Order(
            quentity=5,
            product_id=self.product.id,
            user_id=self.user.id
        )
        storage.new(self.order)
        storage.new(self.product)
        storage.new(self.user)
        storage.save()

    def tearDown(self):
        """Clean up the session."""
        storage.delete(self.order)
        storage.delete(self.product)
        storage.delete(self.user)
        storage.save()

    def test_pep8_conformance_order(self):
        """Test that models/order.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/orders.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_order_attributes(self):
        """Test that Order has the correct attributes."""
        self.assertEqual(self.order.quentity, 5)

    def test_to_dict(self):
        """Test to_dict method on Order."""
        order_dict = self.order.to_dict()
        self.assertIn('quentity', order_dict)
        self.assertIn('product_id', order_dict)
        self.assertIn('user_id', order_dict)


if __name__ == '__main__':
    unittest.main()
