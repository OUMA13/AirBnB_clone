#!/usr/bin/python3

"""
Contains the TestStateDocs classes
"""
import unittest
from models.state import State
from models.engine.file_storage import FileStorage
State = state.State

class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up test environment"""
        self.stt = State()

    def tearDown(self):
        """Clean up test environment"""
        del self.state

    def test_state_attributes_ow(self):
        """Test if State class has the correct attributes"""
        self.assertTrue(hasattr(self.stt, "id"))
        self.assertTrue(hasattr(self.stt, "created_at"))
        self.assertTrue(hasattr(self.stt, "updated_at"))
        self.assertTrue(hasattr(self.stt, "name"))

    def test_state_inheritance_ow(self):
        """Unittests for testing save method of the State class"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_save_ow(self):
        """Test if State instance can be saved to file"""
        FileStorage._FileStorage__objects = {}
        self.state.save()
        self.assertIn(self.state.id, FileStorage._FileStorage__objects)

    def test_state_to_dict_ow(self):
        """Unittests for testing to_dict method of the State class"""
        stt_dct = self.state.to_dict()
        self.assertIsInstance(stt_dct, dict)
        self.assertIn("id", stt_dct)
        self.assertIn("created_at", stt_dct)
        self.assertIn("updated_at", stt_dct)
        self.assertIn("name", stt_dct)


if __name__ == "__main__":
    unittest.main()
