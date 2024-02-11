#!/usr/bin/python3
"""
Define Unittests for models/amenity.py
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity_with_me(unittest.TestCase):
    """Contains the Test cases of Amenity class"""

    def setUp(self):
        """Set up for the test"""
        self.ow_n = "Amenity"
        self.ow_v = Amenity

    def test_name_attri_initialization(self):
        """
        Test if 'name' attribute is initialized propebly
        """
        name = "Wissal"
        amenity_instance = self.ow_v(name=name)
        self.assertEqual(amenity_instance.name, name)

    def test_name_attri(self):
        """
        Test if 'name' attribute is a string
        """
        amenity_instance = self.ow_v()
        self.assertIsInstance(amenity_instance.name, str)

    def test_name_attri_default(self):
        """
        Test if 'name' attribute has default value ''
        """
        amenity_instance = self.ow_v()
        self.assertEqual(amenity_instance.name, '')

    def test_to_dict_method(self):
        """Test the to_dict method if it works fine"""
        amenity_instance = self.ow_v()
        amenity_dict = amenity_instance.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
