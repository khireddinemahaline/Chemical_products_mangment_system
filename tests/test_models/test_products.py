#!/usr/bin/python3
'''
Test_Product
    All the test for the products are implemented here.
'''


import unittest
from models.products import Product
from models.orders import Order
import datetime
from models import storage
import pep8

class TestProduct(unittest.TestCase):
    """Set up a fresh instance for each test."""
    def setUp(self):
        self.product = Product(
            name="Sample Product",
            ref="REF123",
            description="This is a sample product description.",
            quentity=10
        )
        storage.new(self.product)
        storage.save()

    def tearDown(self):
        """clean up the ssesion"""
        storage.delete(self.product)
        storage.save()

    def test_pep8_conformance_product(self):
        """Test that models/product.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/products.py'])
        self.assertEqual(result.total_errors, 0,
                    "Found code style errors (and warnings).")

    def test_create_product(self):
        """test that product is created seccessfuly"""
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, "Sample Product")
        self.assertEqual(self.product.ref, "REF123")
        self.assertEqual(self.product.description, "This is a sample product description.")
        self.assertEqual(self.product.quentity, 10)
    
    def test_default_quantity(self):
        """Test that default quantity is 0 when not provided."""
        product_with_default_quantity = Product(
            name="Default Quantity Product",
            ref="REF456",
            description="Default quantity test"
        )
        storage.new(product_with_default_quantity)
        storage.save()

        self.assertEqual(product_with_default_quantity.quentity, 1)    
