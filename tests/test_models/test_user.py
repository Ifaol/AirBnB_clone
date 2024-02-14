#!/usr/bin/python3
"""Unit tests for the `User` class.
"""
import unittest
from models.user import User
from models import storage
from datetime import datetime

class TestUser(unittest.TestCase):
    """Test cases for the `User` class."""

    def test_user_attributes(self):
        """Test if user attributes are correctly initialized."""

        user = User()
        k = f"{type(user).__name__}.{user.id}"
        self.assertIn(k, storage.all())
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_instance(self):
        """Test if user instance is created with correct attributes."""

        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_str_representation(self):
        """Test if user instance string representation is correct."""

        user = User()
        string = f"[{type(user).__name__}] ({user.id}) {user.__dict__}"
        self.assertEqual(user.__str__(), string)

    def test_user_save_method(self):
        """Test if user save method updates `updated_at` attribute."""

        user = User()
        old_update = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_update)

    def test_user_to_dict_method(self):
        """Test if user `to_dict` method returns the correct dictionary."""

        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], type(user).__name__)
        self.assertIn('created_at', user_dict.keys())
        self.assertIn('updated_at', user_dict.keys())
        self.assertNotEqual(user, user_dict)

if __name__ == "__main__":
    unittest.main()

