#!/usr/bin/python3

"""
define unitest for models state.py
"""
import unittest
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """unittest for testing instantiation of the state class"""

    def setUp(self):
        """Set up test environment"""
        self.stt = State()

    def tearDown(self):
        """Clean up test environment"""
        del self.stt

    def test_state_attributes_ow(self):
        """Test if State class has the correct attributes"""
        self.assertTrue(hasattr(self.stt, "id"))
        self.assertTrue(hasattr(self.stt, "created_at"))
        self.assertTrue(hasattr(self.stt, "updated_at"))
        self.assertTrue(hasattr(self.stt, "name"))

    def test_state_inheritance_ow(self):
        """Unittests for testing save method of the State class"""
        self.assertTrue(issubclass(State, BaseModel))
    
    def test_default_name_ow(self):
        """test if the name attribute ia ans empty string"""
        self.assertEqual(self.stt.name, "")

    def test_update_name_ow(self):
        """test if name attribute can be updatedd"""
        self.stt.name = "Meknes"
        self.assertEqual(self.stt.name, "Meknes")

    def test_to_dict_returns_dict_ow(self):
        """Test if to_dict method will possibly returns a dictionary"""
        stt_dict = self.stt.to_dict()
        self.assertIsInstance(stt_dict, dict)

    def test_to_dict_all_attr_ow(self):
        """test to dict method will return all the attribte """
        self.stt.name = "wISSAL"
        stt_dict = self.stt.to_dict()
        self.assertIn("name", stt_dict)
        stt_dict = self.stt.to_dict()
        self.assertIn("id", stt_dict)
        self.assertIn("created_at", stt_dict)
        self.assertIn("updated_at", stt_dict)
        self.assertIn("name", stt_dict)



if __name__ == "__main__":
    unittest.main()
