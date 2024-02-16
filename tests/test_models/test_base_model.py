#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime

class TestModelBasics(unittest.TestCase):
    """Testing for basic functionality of BaseModel"""

    def setUp(self):
        """Set up test fixtures."""
        self.base1 = BaseModel()
        self.base2 = BaseModel(**self.base1.to_dict())
        self.base3 = BaseModel("hello", "wait", "in")

    def tearDown(self):
        """Tear down test fixtures."""
        del self.base1
        del self.base2
        del self.base3

    def test_attributes(self):
        """Test instance attributes."""
        key = f"{type(self.base1).__name__}.{self.base1.id}"
        self.assertIn(key, storage.all())
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base1.updated_at, datetime)
        self.assertEqual(self.base1.created_at, self.base2.created_at)
        self.assertEqual(self.base1.id, self.base2.id)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        base_dict = self.base1.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], type(self.base1).__name__)
        self.assertIn('created_at', base_dict.keys())
        self.assertIn('updated_at', base_dict.keys())
        self.assertNotEqual(self.base1, self.base2)

    def test_save_method(self):
        """Test save method."""
        old_update = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(self.base1.updated_at, old_update)

    def test_string_representation(self):
        """Test string representation."""
        string = f"[{type(self.base1).__name__}] ({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(self.base1.__str__(), string)

if __name__ == "__main__":
    unittest.main()

