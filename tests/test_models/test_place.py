#!/usr/bin/python3
"""Unit tests for the `Place` class.
"""
import unittest
from models.place import Place
from models import storage
from datetime import datetime

class TestPlaceAttributes(unittest.TestCase):
    """Test case for checking attributes of the `Place` class."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.place = Place()

    def test_instance_attributes(self):
        """Test instance attributes."""
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_instance_creation(self):
        """Test instance creation."""
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_string_representation(self):
        """Test string representation."""
        string = f"[{type(self.place).__name__}] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(self.place.__str__(), string)

    def test_save_method(self):
        """Test save method."""
        old_update = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_update)

    def test_to_dict_method(self):
        """Test to_dict method."""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], type(self.place).__name__)
        self.assertIn('created_at', place_dict.keys())
        self.assertIn('updated_at', place_dict.keys())
        self.assertNotEqual(self.place, Place(**place_dict))

if __name__ == "__main__":
    unittest.main()

