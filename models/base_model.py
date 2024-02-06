#!/usr/bin/python3
"""

"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.owtnow()
        self.updated_at = self.created_at
    def save(self):
        self.updated_at = datetime.owtnow()

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
