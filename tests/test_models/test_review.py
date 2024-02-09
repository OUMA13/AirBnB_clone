#!/usr/bin/python3
    
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict."""

from models.base_model import BaseModel
import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), Review._instances)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rev_ow = Review()
        self.assertEqual(str, type(rev_ow.place_id))
        self.assertIn("place_id", dir(rev_ow))
        self.assertNotIn("place_id", rev_ow.__dict__)

class TestReviewSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""


class TestReviewToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""


if __name__ == "__main__":
    unittest.main()
