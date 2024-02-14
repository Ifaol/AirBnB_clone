#!/usr/bin/python3
"""Unit testing for the `Amenity` class."""
import unittest
from models.amenity import Amenity
from models import storage
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.amenity1 = Amenity()
        self.amenity2 = Amenity(**self.amenity1.to_dict())
        self.amenity3 = Amenity("test", "data", "here")

    def tearDown(self):
        """Tear down test fixtures."""
        del self.amenity1
        del self.amenity2
        del self.amenity3

    def test_attribute_types(self):
        """Test attribute types."""
        key = f"{type(self.amenity1).__name__}.{self.amenity1.id}"
        self.assertIsInstance(self.amenity1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(self.amenity3.name, "")

    def test_initialization(self):
        """Test instance initialization."""
        self.assertIsInstance(self.amenity1.id, str)
        self.assertIsInstance(self.amenity1.created_at, datetime)
        self.assertIsInstance(self.amenity1.updated_at, datetime)
        self.assertEqual(self.amenity1.updated_at, self.amenity2.updated_at)

    def test_string_representation(self):
        """Test string representation."""
        string = f"[{type(self.amenity1).__name__}] ({self.amenity1.id}) {self.amenity1.__dict__}"
        self.assertEqual(self.amenity1.__str__(), string)

    def test_save_method(self):
        """Test save method."""
        old_update = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.updated_at, old_update)

    def test_to_dict_method(self):
        """Test to_dict method."""
        amenity_dict = self.amenity2.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], type(self.amenity2).__name__)
        self.assertIn('created_at', amenity_dict.keys())
        self.assertIn('updated_at', amenity_dict.keys())
        self.assertNotEqual(self.amenity1, self.amenity2)

if __name__ == "__main__":
    unittest.main()

