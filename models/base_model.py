#!/usr/bin/python3
"""
    this Module support the BaseModel Class as the parent Class for all the Inheritate instance
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """ The base Class for all the inheritate attribute """

    def __init__(self, *args, **kwargs):
        """Inisialization of attribues of the BaseModel Class"""
        
        isof = "%Y-%m-%dT%H:%M:%S.%f"
        
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for ow_k, ow_v in kwargs.items():
                if ow_k == 'created_at' or ow_k == 'updated_at':
                    setattr(self, ow_k, datetime.strptime(ow_v, isof))
                elif ow_k != '__class__':
                    setattr(self, ow_k, ow_v)
    
    def save(self):
        """  it updates the instance is attribute updated_at with the current date time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys and values of __dict__ 
        of the instance in the base class including __class__ update_at and create_at"""
        data = {}
        for k, v in self.__dict__.items():
            if k == 'created_at':
                v = v.isoformat()
            if k == 'updated_at':
                v = v.isoformat()
            data[k] = v
        data['__class__'] = self.__class__.__name__
        return data

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
