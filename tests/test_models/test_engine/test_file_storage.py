#!/usr/bin/python3
""" Module for testing File.storage file """

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage_file_with_me(unittest.TestCase):
    """ class that includes all testing units for the file storage"""
    def setUp(self):
        """setup for the testes"""
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.storage.new(self.model1)
        self.storage.new(self.model2)
        self.storage.save()

    def tearDown(self):
        """Remove the test file after every test"""
        del self.storage
        del self.model1
        del self.model2

    def test_all_method_by_adding_storage(self):
        """Test the all method by adding some objects to storage"""
        self.storage._FileStorage__objects = {}
        ow_obj1 = BaseModel()
        ow_obj2 = User()
        self.storage.new(ow_obj1)
        self.storage.new(ow_obj2)
        self.storage.save()
        self.assertEqual(len(self.storage.all()), 4)

    def test_new_method_in_thefile_storage(self):
        """ Testing the new method if it wokrs just fine"""
        ow_obj = BaseModel()
        self.storage.new(ow_obj)
        self.storage.save()
        self.assertIn(ow_obj, self.storage.all().values())

    def test_save_if_it_saves(self):
        """ Test the save method if it saves propebly
            and we check if the saving it exist after the save
        """
        ow_obj = BaseModel()
        self.storage.new(ow_obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """test the reload method if it reloaded objects properly"""
        storage_copy = FileStorage()
        storage_copy.reload()
        model1_id = "{}.{}".format(type(self.model1).__name__, self.model1.id)
        model2_id = "{}.{}".format(type(self.model2).__name__, self.model2.id)
        self.assertIn(model1_id, storage_copy.all())
        self.assertIn(model2_id, storage_copy.all())
        reloaded_model1 = storage_copy.all()[model1_id]
        reloaded_model2 = storage_copy.all()[model2_id]
        self.assertIsInstance(reloaded_model1, BaseModel)
        self.assertIsInstance(reloaded_model2, BaseModel)
        self.assertEqual(reloaded_model1.id, self.model1.id)
        self.assertEqual(reloaded_model2.id, self.model2.id)


if __name__ == '__main__':
    unittest.main()
