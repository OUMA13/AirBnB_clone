#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation_att(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates_ow(self):
       """ verify that instantiating a User object without any arg return an obt type User"""

        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects_ow(self):
        """ Ensure that anewly instantiated User objt is stored in the objts att of the modals.storage"""
       
       self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str_ow(self):
        """ confirme that the id attr of a User objt is a string """

        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """validate that the created_at attr of the user objt is of type dt"""

        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """ensur that the uptd_at att of a user objt is of type dt"""

        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """ assert that the  email att of a user objt is str"""

        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """verify that the password attr of a user objt is a str"""

        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """ensur that the first_name attr of a user objt is a string"""

        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """ confirme that the last_ name attr of a user objt is a str"""

        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        """ ensure that the two different user objt have unique id att"""

        user_ow = User()
        userk = User()
        self.assertNotEqual(user_ow.id, userk.id)

    def test_two_users_different_created_at(self):
        """ validate dat two diff us objt have diff created_at """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """ ensure that two diff user objt have diff updtd_at"""

        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        """ test the string representation of a user objt"""

        dt_ow = datetime.today()
        dt_ow_repr = repr(dt_ow)
        us_w = User()
        us_w.id = "123456"
        us_w.created_at = us_w.updated_at = dt_ow
        us_str = us_w.__str__()
        self.assertIn("[User] (123456)", us_str)
        self.assertIn("'id': '123456'", us_str)
        self.assertIn("'created_at': " + dt_ow_repr, us_str)
        self.assertIn("'updated_at': " + dt_ow_repr, us_str)

    def test_args_unused(self):
        """ verify that pass non as an arg to the user cntrctr doesen't affect the object"""
        us_w = User(None)
        self.assertNotIn(None, us_w.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """test instantiation of a user objt with keyword arg"""

        dt_ow = datetime.today()
        dt_iso = dt_ow.isoformat()
        us_w = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us_w.id, "345")
        self.assertEqual(us_w.created_at, dt_ow)
        self.assertEqual(us_w.updated_at, dt_ow)

    def test_instantiation_with_None_kwargs(self):
        """ensur that passing none as a keyword arg raises a typError"""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save_att(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    def setUp(self):
       """ prepar the envr beforr eachh test case by renaming the exesting file.json to tmp"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """ Clean up the environment after each test case by removing the "file.json" and renaming "tmp" back to "file.json" (if "tmp" exists)"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_A__save(self):
""" verify that calling the save meth upt the updated_at att of a user objt"""
        us_w = User()
        sleep(0.05)
        first_updated_at = us_w.updated_at
        us_w.save()
        self.assertLess(first_updated_at, us_w.updated_at)

    def test_B__saves(self):
        """Ensure that successive calls to the save meth upt the updated_at att  of a User objt"""
        us_w = User()
        sleep(0.05)
        first_updated_at = us_w.updated_at
        us_w.save()
        second_updated_at = us_w.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us_w.save()
        self.assertLess(second_updated_at, us_w.updated_at)

    def test_save_with_arg(self):
        """validat that passing an arg to the save meth 
        raises a TypError"""
        us_w = User()
        with self.assertRaises(TypeError):
            us_w.save(None)

    def test_save_updates_file(self):
        """ nsure that calling the save method updt 
        the "file.json" with the new User obj"""
        us_w = User()
        us_w.save()
        usda = "User." + us_w.id
        with open("file.json", "r") as f:
            self.assertIn(usda, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        us_w = User()
        self.assertIn("id", us_w.to_dict())
        self.assertIn("created_at", us_w.to_dict())
        self.assertIn("updated_at", us_w.to_dict())
        self.assertIn("__class__", us_w.to_dict())

    def test_to_dict_contains_added_attributes(self):
        us_w = User()
        us_w.middle_name = "Holberton"
        us_w.my_number = 98
        self.assertEqual("Holberton", us_w.middle_name)
        self.assertIn("my_number", us_w.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        us_w = User()
        user_dict = us_w.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dati = datetime.today()
        us_w = User()
        us_w.id = "123456"
        us_w.created_at = us_w.updated_at = dati
        tdict_att = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dati.isoformat(),
            'updated_at': dati.isoformat(),
        }
        self.assertDictEqual(us_w.to_dict(), tdict_att)

    def test_contrast_to_dict_dunder_dict(self):
        us_w = User()
        self.assertNotEqual(us_w.to_dict(), us_w.__dict__)

    def test_to_dict_with_arg(self):
        us_w = User()
        with self.assertRaises(TypeError):
            us_w.to_dict(None)


if __name__ == "__main__":
    unittest.main()
