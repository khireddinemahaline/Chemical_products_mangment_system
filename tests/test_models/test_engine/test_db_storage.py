#!/usr/bin/python3
"""
Test_DBStorage
All the tests for the DBStorage are implemented here.
"""

import unittest
import inspect
import pep8  # Ensure you have pep8 installed
from models.engine.db_storage import DBStorage
from models.users import User
from models.products import Product
from models import storage  # Assuming you have a storage instance


class TestDBStorageDocs(unittest.TestCase):
    """
    Tests to check the documentation and style of the DBStorage class.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests."""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """
        Test that models/engine/db_storage.py conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """
        Test tests/test_models/test_engine/test_db_storage.py conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        path = 'tests/test_models/test_engine/test_db_storage.py'
        result = pep8s.check_files([path])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDBStorage(unittest.TestCase):
    """
    Tests for the DBStorage class methods.
    """

    def setUp(self):
        """
        Set up test environment before each test.
        Initialize DBStorage, create test user and product.
        """
        self.storage = DBStorage()
        self.storage.reload()

        # Create a new user and product for testing
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            _password="password123",
            role="professor"
        )
        self.product = Product(
            name="Test Product",
            ref="testref",
            description="Test description",
            quentity=10
        )
        self.storage.new(self.product)
        self.storage.new(self.user)
        self.storage.save()

    def tearDown(self):
        """
        Clean up the test environment after each test.
        Delete test user and product from storage.
        """
        self.storage.delete(self.user)
        self.storage.delete(self.product)
        self.storage.save()

    def test_get(self):
        """
        Test the get method in DBStorage.
        Ensure the correct object is retrieved based on ID.
        """
        user = self.storage.get(User, self.user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user.id, self.user.id)

        # Test with non-existing ID
        non_existing = self.storage.get(User, "fake_id")
        self.assertIsNone(non_existing)

    def test_count(self):
        """
        Test the count method in DBStorage.
        Check if counting objects in the storage works as expected.
        """
        initial_count = self.storage.count(User)
        self.assertEqual(initial_count, 1)

        # Create a new user and check the count again
        new_user = User(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            _password="testpass2",
            role="lab manager"
        )
        self.storage.new(new_user)
        self.storage.save()

        self.assertEqual(self.storage.count(User), initial_count + 1)

        # Test count for a specific class (Product)
        product_count = self.storage.count(Product)
        self.assertEqual(product_count, 1)

        # Test overall count of all objects
        total_count = self.storage.count()
        self.assertEqual(total_count, 3)  # Two users and one product


if __name__ == "__main__":
    unittest.main()
