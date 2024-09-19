#!/usr/bin/python3
"""
Test_User
    All the tests for the User model are implemented here.
"""

import unittest
from models.users import User
import pep8
from models import storage

class TestUser(unittest.TestCase):
    """Tests for the User model."""
    def setUp(self):
        """Set up a fresh instance before each test."""
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            user_password="password123",
            role="professor"
        )
        storage.new(self.user)
        storage.save()

    def tearDown(self):
        """Clean up the session."""
        storage.delete(self.user)
        storage.save()

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/users.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_attributes(self):
        """Test that User has the correct attributes."""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.role, "professor")

    def test_password_hashing(self):
        """Test that password hashing works."""
        raw_password = "password123"
        self.assertTrue(self.user.check_password(raw_password))

    def test_to_dict(self):
        """Test to_dict method on User."""
        user_dict = self.user.to_dict()
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('email', user_dict)
        self.assertNotIn('_password', user_dict)


if __name__ == '__main__':
    unittest.main()
