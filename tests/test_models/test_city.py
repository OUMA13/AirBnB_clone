#!/usr/bin/python3
"""
this Module define the Unittests( tast different cases) for models/city.py
"""

from models.base_model import BaseModel
from models.city import City
import unittest


class test_City_Uni(unittest.TestCase):
    """Contains the TestCity test cases/unit tests classes """

    def __init__(self, *args, **kwargs):
        """Preparing the test inisialization """

        super().__init__(*args, **kwargs)
        self.ow_n = "City"
        self.ow_v = City

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

    def test_name_initial_value(self):
        """
        test if state id attribute in an instance of the City
        is initially an empty string
        """
        city_instance = self.value()
        self.assertEqual(city_instance.name, "")

    def test_state_id_initial_value(self):
        """
        test if state id attribute in an instance of the City
        is initially an empty string
        """
        city_instance = self.value()
        self.assertEqual(city_instance.state_id, "")
