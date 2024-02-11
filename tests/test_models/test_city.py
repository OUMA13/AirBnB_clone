#!/usr/bin/python3
"""
this Module define the Unittests( tast different cases) for models/city.py
"""

from models.base_model import BaseModel
from models.city import City
import unittest


class test_City_Uni(unittest.TestCase):
    """Contains the TestCity test cases/unit tests classes """

    def setUp(self):
        """Set up for the test"""
        self.ow_n = "City"
        self.ow_v = City

    def value(self):
        """
        Helper method that return City class
        """
        return self.ow_v()

    def test_state_id_isan_instance(self):
        """
        test if state id attribute in an instance
        of the City represent a string
        """
        city_instance = self.value()
        self.assertEqual(type(city_instance.state_id), str)

    def test_name_isan_insatance(self):
        """
        test if name attribute in an instance
        of the City represent a string
        """
        city_instance = self.value()
        self.assertEqual(type(city_instance.name), str)

    def test_city_with_no_args(self):
        """ test City wthout arguments"""
        self.assertEqual(City, type(City()))

    def test_name_initial_empty_string(self):
        """
        test if state id attribute in an instance of the City
        is initially an empty string
        """
        city_instance = self.value()
        self.assertEqual(city_instance.name, "")

    def test_state_id_initial_empty_string(self):
        """
        test if state id attribute in an instance of the City
        is initially an empty string
        """
        city_instance = self.value()
        self.assertEqual(city_instance.state_id, "")

    def test_city_attributes_state_id_name(self):
        """
        test if the city instance has the attribute state id and name
        """
        city_instance = self.value()
        self.assertTrue(hasattr(city_instance, 'state_id'))
        self.assertTrue(hasattr(city_instance, 'name'))


if __name__ == '__main__':
    unittest.main()
