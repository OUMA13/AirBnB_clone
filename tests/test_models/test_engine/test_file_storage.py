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

    def tearDown(self):
        """Remove the test file after every test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_FileStorage_without_arguments(self):
        """test fileStorage without arguments """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_is_file_path_astring(self):
        """ test file storage is file path file_path is a string """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_is_object_adic(self):
        """test __objects is private attribute"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(self.storage), FileStorage)

    def test_FileStorage_instantiatio_no_args(self):
        """ test instantiation with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all_method_by_adding_storage(self):
        """Test the all method by adding some objects to storage"""
        ow_obj1 = BaseModel()
        ow_obj2 = User()
        self.storage.new(ow_obj1)
        self.storage.new(ow_obj2)
        self.assertEqual(len(self.storage.all()), 2)

    def test_all_method(self):
        """test all method if it works fine"""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new_method_in_thefile_storage(self):
        """ Testing the new method if it wokrs just fine"""
        ow_obj = BaseModel()
        self.storage.new(ow_obj)
        self.assertIn(ow_obj, self.storage.all().values())

    def test_new_method_witharguments(self):
        """ test new method with arguments """
        with self.assertRaises(TypeError):
            self.storage.new(BaseModel(), 1)

    def test_save_create_file_exists(self):
        """tests if the file was created with the same name"""
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_if_it_saves(self):
        """ Test the save method if it saves propebly
            and we check if the saving it exist after the save
        """
        ow_obj = BaseModel()
        self.storage.new(ow_obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_witharguments(self):
        """test the reload method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    def test_reload_without_file_exist(self):
        """
            Test what would happen if file.json does not exists
            and is reloaded
        """

        try:
            self.storage.reload()
            self.assertTrue(True)
        except FileNotFoundError:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
