#!/usr/bin/python3
""" testing the place """
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlacedocumentation(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""

    def __init__(self, *args, **kwargs):
        """Special method used for initializing objects"""
        super().__init__(*args, **kwargs)
        self.ow_name = "Place"
        self.ow_value = Place

    def test_city_id_oattw(self):
        """Write a test case for the city_id attribute of your Place class"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.city_id), str)

    def test_user_id_oattw(self):
        """Test Place has attr user_id, and it's an empty string"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.user_id), str)

    def test_name_oattw(self):
        """Test Place has attribute name, and it's an empty string"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.name), str)

    def test_description_oattw(self):
        """The test location is an empty string"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.description), str)

    def test_number_rooms_oattw(self):
        """To test the number_rooms attribute of your Place class,
        you can add a method called test_number_rooms
        inside your TestPlace class."""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.number_rooms), int)

    def test_number_bathrooms_oattw(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.number_bathrooms), int)

    def test_max_guest_oattw(self):
        """Test Place has attr max_guest"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.max_guest), int)

    def test_price_by_night_oattw(self):
        """Test Place has attr price_by_night"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.price_by_night), int)

    def test_latitude_oattw(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.latitude), float)

    def test_longitude_oattw(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.longitude), float)

    def test_amenity_ids_oattw(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        nw_el = self.ow_value()
        nw_el.save()
        self.assertEqual(type(nw_el.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
