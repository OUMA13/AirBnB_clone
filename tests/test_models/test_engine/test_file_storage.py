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
