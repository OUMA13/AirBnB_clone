#!/usr/bin/python3
"""

"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity_Uni(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.ow_n = "Amenity"
        self.ow_v = Amenity

    def test_nameB(self):
        """ """
        owi = self.value()
        self.assertEqual(type(owi.name), str)
