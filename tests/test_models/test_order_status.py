#!/usr/bin/python3
"""
Test_OrderStatus
    All the tests for the Order_status model are implemented here.
"""

import unittest
import pep8
from models import storage, User, Order, Product, Order_status

class TestOrderStatus(unittest.TestCase):
    """Tests for the Order_status model."""
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

        self.order_status = Order_status(
            order_id=self.order.id,
            status="pending"
        )

        storage.new(self.order)
        storage.new(self.product)
        storage.new(self.user)
        storage.new(self.order_status)
        storage.save()

    def tearDown(self):
        """Clean up the session."""
        storage.delete(self.order)
        storage.delete(self.product)
        storage.delete(self.user)
        storage.delete(self.order_status)
        storage.save()

    def test_pep8_conformance_order_status(self):
        """Test that models/order_status.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files

    def test_confirmed(self):
        self.order_status.status = "confirmed"
        self.assertEqual(self.order_status.status, 'confirmed')