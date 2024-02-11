#!/usr/bin/python3
"""
Define Unittests for models/amenity.py
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


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

    def test_created_at_datetime_attribute(self):
        """ test the crreate at attribute of amenity"""
        self.assertEqual(datetime, type(self.ow_v().created_at))

    def test_to_dict_method(self):
        """Test the to_dict method if it works fine"""
        ow_amenity_inst = self.ow_v()
        ow_amenity_dict = ow_amenity_inst.to_dict()
        self.assertIsInstance(ow_amenity_dict, dict)
        self.assertEqual(ow_amenity_dict['__class__'], 'Amenity')

    def test_without__arguments_inis(self):
        """ test without arguments initialize"""
        self.assertEqual(self.ow_v, type(self.ow_v()))


if __name__ == '__main__':
    unittest.main()
