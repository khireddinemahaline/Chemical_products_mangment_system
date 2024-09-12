#!/usr/bin/python3
'''
Test_BaseModel
    All the test for the base_model are implemented here.
'''


import unittest
from models.base_model import BaseModel, Base
from datetime import datetime
from uuid import uuid4
import pep8


class TestBaseModel(unittest.TestCase):
    """
    test basemode:
    - test data type of arguments
    """
    def setUp(self):
        """Set up a fresh instance before each test"""
        self.model = BaseModel()

    def test_pep8_conformance_basemodel(self):
        """Test that models/basemodel.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_initialization(self):
        """Ensure that the instance is correctly initialized with a UUID,
        current created_at, and updated_at timestamps."""
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_unpacking_kwarg(self):
        """test unpaching method"""
        kwarg_test = {
            'id': '123',
            'created_at': '2024-09-01T12:00:00.000000',
            'updated_at': '2024-09-01T12:01:00.000000'
        }
        model = BaseModel(**kwarg_test)
        self.assertEqual(model.id, '123')
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, datetime(2024, 9, 1, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2024, 9, 1, 12, 1, 0))

    def test_str_method(self):
        """Test the string representation of BaseModel"""
        model = str(self.model)
        expected = (
            "[{}] ({}) {{'id':{}, 'created_at':{}, 'updated_at':{}}}".format(
                self.model.__class__.__name__,
                repr(self.model.id),
                repr(self.model.id),
                repr(self.model.created_at),
                repr(self.model.updated_at))
        )
        self.assertEqual(model, expected)

    def test_save_method(self):
        """Test the save method"""
        time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(time, self.model.updated_at)
        self.assertGreater(self.model.updated_at, time)

    def test_to_dict(self):
        """Test that to_dict returns a proper dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        created_at = self.model.created_at.isoformat()
        update_at = self.model.updated_at.isoformat()
        self.assertEqual(model_dict['created_at'], created_at)
        self.assertEqual(model_dict['updated_at'], update_at)
        self.assertNotIn('_sa_instance_state', model_dict)

    def test_iso_date_format_in_to_dict(self):
        """Test that created_at and updated_at are in ISO format in to_dict"""
        model_dict = self.model.to_dict()
        created_at = self.model.created_at.isoformat()
        update_at = self.model.updated_at.isoformat()
        self.assertEqual(model_dict['created_at'], created_at)
        self.assertEqual(model_dict['updated_at'], update_at)


if __name__ == '__main__':
    unittest.main()
