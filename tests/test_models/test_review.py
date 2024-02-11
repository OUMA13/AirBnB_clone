#!/usr/bin/python3

"""Defines unittests for models/review.py.

Unittest classes:
    - TestReviewInstantiation: Tests the instantiation of the Review class.
    - TestReviewSave: Tests the save method of the Review class.
    - TestReviewToDict: Tests the to_dict method of the Review class.
"""

from models.base_model import BaseModel
import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_review_with_no_args_(self):
        """Test if Review instance is created with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_if_id_is_public_string(self):
        """test if the id is a pubklic string"""
        self.assertEqual(str, type(Review().id))

    def test_two_id_reviews(self):
        """ test if two reviews have different ids"""
        ow_rev1 = Review()
        ow_rev2 = Review()
        self.assertNotEqual(ow_rev1.id, ow_rev2.id)

    def test_created_at_datetime(self):
        """ test created at is a public datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_datetime(self):
        """test updated at is a public datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_work(self):
        """test place id if it is a public class attribute"""
        rev_ow = Review()
        self.assertEqual(str, type(rev_ow.place_id))
        self.assertIn("place_id", dir(rev_ow))
        self.assertNotIn("place_id", rev_ow.__dict__)


if __name__ == "__main__":
    unittest.main()
