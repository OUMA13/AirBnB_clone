#!/usr/bin/python3
"""
Define Unittests for models/amenity.py
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity_Uni(test_basemodel):
    """Contains the TestAmenityDocs classes """

    def __init__(self, *args, **kwargs):
        """preparing the test and preparing to carry out the required                        tests """

        super().__init__(*args, **kwargs)
        self.ow_n = "Amenity"
        self.ow_v = Amenity

    def test_nameB(self):
        """
        attribute in the instance of the Amenity model represents a string or not, thus validating the definition of this attribute in the model
        """
        owi = self.value()
        self.assertEqual(type(owi.name), str)
