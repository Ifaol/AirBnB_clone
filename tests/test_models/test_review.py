#!/usr/bin/python3
"""Custom unit tests for the `Review` class."""

import unittest
from models.review import Review
from models import storage
from datetime import datetime

class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    def setUp(self):
        """Set up testing environment."""
        self.review_1 = Review()
        self.review_2 = Review(**self.review_1.to_dict())
        self.review_3 = Review("Good place", "user123", "place456")

    def tearDown(self):
        """Tear down testing environment."""
        del self.review_1
        del self.review_2
        del self.review_3

    def test_params(self):
        """Test method for class attributes."""
        self.assertIsInstance(self.review_1.text, str)
        self.assertIsInstance(self.review_1.user_id, str)
        self.assertIsInstance(self.review_1.place_id, str)
        self.assertIn(f"Review.{self.review_1.id}", storage.all())
        self.assertEqual(self.review_3.text, "Good place")

    def test_init(self):
        """Test method for public instances."""
        self.assertIsInstance(self.review_1.id, str)
        self.assertIsInstance(self.review_1.created_at, datetime)
        self.assertIsInstance(self.review_1.updated_at, datetime)
        self.assertEqual(self.review_1.updated_at, self.review_2.updated_at)

    def test_str(self):
        """Test method for str representation."""
        expected_string = f"[Review] ({self.review_1.id}) {self.review_1.__dict__}"
        self.assertEqual(self.review_1.__str__(), expected_string)

    def test_save(self):
        """Test method for save."""
        old_update = self.review_1.updated_at
        self.review_1.save()
        self.assertNotEqual(self.review_1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict."""
        review_dict = self.review_2.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('created_at', review_dict.keys())
        self.assertIn('updated_at', review_dict.keys())
        self.assertNotEqual(self.review_1, self.review_2)


if __name__ == "__main__":
    unittest.main()

