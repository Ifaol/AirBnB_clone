#!/usr/bin/python3
"""Unit tests for the `State` class.
"""
import unittest
from models.state import State
from models import storage
from datetime import datetime

class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        """Set up test fixtures."""
        self.state1 = State()
        self.state2 = State(**self.state1.to_dict())
        self.state3 = State("Test State")

    def test_attributes(self):
        """Test attributes of the `State` class."""
        self.assertIsInstance(self.state1.id, str)
        self.assertIsInstance(self.state1.created_at, datetime)
        self.assertIsInstance(self.state1.updated_at, datetime)
        self.assertEqual(self.state1.updated_at, self.state2.updated_at)
        self.assertIsInstance(self.state1.name, str)
        self.assertEqual(self.state3.name, "Test State")

    def test_string_representation(self):
        """Test string representation of the `State` class."""
        string = f"[{type(self.state1).__name__}] ({self.state1.id}) {self.state1.__dict__}"
        self.assertEqual(str(self.state1), string)

    def test_save_method(self):
        """Test the `save` method of the `State` class."""
        old_update = self.state1.updated_at
        self.state1.save()
        self.assertNotEqual(self.state1.updated_at, old_update)

    def test_to_dict_method(self):
        """Test the `to_dict` method of the `State` class."""
        state_dict = self.state2.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], type(self.state2).__name__)
        self.assertIn('created_at', state_dict.keys())
        self.assertIn('updated_at', state_dict.keys())
        self.assertNotEqual(self.state1, self.state2)

if __name__ == "__main__":
    unittest.main()

