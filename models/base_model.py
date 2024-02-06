#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *arg, **kwargs):
        """Inisialization of attribues of the BaseModel Class"""
        isof = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for ow_k, ow_v in kwargs.items():
                if ow_k == 'created_at' or ow_k == 'updated_at':
                    setattr(self, ow_k, datetime.strptime(ow_v, isof))
                elif ow_k != '__class__':
                    setattr(self, ow_k, ow_v)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = {}
        for k, v in self.__dict__.items():
            if k == 'created_at':
                v = v.isoformat()
            if k == 'updated_at':
                v = v.isoformat()
            data[k] = v
        return data

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
