#!/usr/bin/python3

"""Test BasModel for exepted behavior and documentation"""
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
BaseModel_w = models.base_model.BaseModel
module_doc = models.base_model.__doc__

class TestBaseModel_dt(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""
    

    def setUp(self):
        """Set up for the test
        Test the behavior of the 'updated_at' attribute in the BaseModel class
        """
        self.base_doc_set = BaseModel_w()

    def tearDown(self):
        """Cleaning process after each individual test case """
        del self.base

    def test_instance_crt(self):
        """test that the base attri is an instnce of a BaseModel """
        self.assertIsInstance(self.base, BaseModel)

    def test_id_generation_ID(self):
        """test that the id attri of basmodel instc 
        has been created correctly  """
        self.assertIsNotNone(self.base.id)
        self.assertIsInstance(self.base.id, str)

    def test_created_atT(self):
        """This test verifies that the 'created_at' attribute of the 'base' instance, assumed to be set up in the test environment, 
    is an instance of datetime.datetime. It ensures that the creation timestamp is stored correctly upon instance creation """

        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_attribute(self):
        """This test verifies that the 'updated_at' attribute of the 'base' instance, assumed to be set up in the test environment,
    is an instance of datetime.datetime. It ensures that the update timestamp is stored correctly upon instance creation """

        self.assertIsInstance(self.base.updated_at, datetime)

    def test_save_str(self):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        up_updated_attribute = self.base.updated_at
        self.base.save()
        self.assertNotEqual(up_updated_attribute, self.base.updated_at)

    def test_to_dict_instance(self):
        """"""
        dict_ow = self.base.to_dict()
        self.assertIsInstance(dict_ow, dict)
        self.assertIn('__class__', dict_ow)
        self.assertIn('id', dict_ow)
        self.assertIn('created_at', dict_ow)
        self.assertIn('updated_at', dict_ow)

    def test_delete_upt(self):
        """"""
       
        models.storage.new(self.base)
        models.storage.save()
        models.storage.delete(self.base)
        self.assertNotIn(self.base, models.storage.all().values())

class TestBaseModelExtended_ow(unittest.TestCase):
    """Test cases for the extended functionalities of the BaseModel class"""

    def test_default_constructor(self):
        """"""
        w = BaseModel()
        self.assertEqual(type(w), BaseModel)

    def test_kwargs_constr(self):
        """"""
        w = BaseModel()
        past = w.to_dict()
        non = BaseModel(**past)
        self.assertFalse(non is w)

    def test_kwargs_integer_cnstrctr(self):
        """"""
        w = BaseModel()
        past = w.to_dict()
        past.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**past)

    def test_save_json(self):
        """updates the public instance attribute updated_at """
        w = BaseModel()
        w.save()
        ow_k = 'BaseModel.' + w.id
        with open('file.json', 'r') as f:
            o = json.load(f)
            self.assertEqual(o[ow_k], o.to_dict())

    def test_str_rep_corre(self):
        """test that the str method has the correct output"""
        new = BaseModel()
        out_ow = "[BaseModel] ({}) {}".format(new.id, new.__dict__)
        self.assertEqual(out_ow, str(new))


    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        w = BaseModel()
        o = w.to_dict()
        self.assertEqual(w.to_dict(), o)

    def test_kwargs_none(self):
        """"""
        ow = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**ow)

    def test_kwargs_one(self):
        """Test constructor with one kwargs"""
        ow = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**ow)

    def test_id(self):
        """ test that the id attr of type str """
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at_type(self):
        """ this  test ensure that when a new inst of basmodel 
        is created, the created_at attri  """
        non = BaseModel()
        self.assertEqual(type(non.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test the behavior of the updated_at attri in the Basemodel class  """
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)

        import time
        time.sleep(1)
        new.save()

        w = new.to_dict()
        non = BaseModel(**w)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
