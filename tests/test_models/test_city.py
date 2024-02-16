#!/usr/bin/python3
"""Custom test cases for City class."""

import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_city_attributes(self):
        """Test City class attributes."""
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, "")
        city.name = "Abuja"
        self.assertEqual(city.name, "Abuja")

    def test_city_instance(self):
        """Test City class instance creation."""
        city1 = City()
        city2 = City(**city1.to_dict())
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city1.created_at, datetime)
        self.assertIsInstance(city1.updated_at, datetime)
        self.assertEqual(city1.updated_at, city2.updated_at)

    def test_city_save(self):
        """Test City class save method."""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, old_updated_at)

    def test_city_to_dict(self):
        """Test City class to_dict method."""
        city1 = City()
        city2 = City(**city1.to_dict())
        city_dict = city1.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('created_at', city_dict.keys())
        self.assertIn('updated_at', city_dict.keys())
        self.assertNotEqual(city1, city2)

if __name__ == "__main__":
    unittest.main()

