#!/usr/bin/python3
"""This module defines a class User and it attribute"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This class inherit fron the BaseModel and
    it defines a user by different attributes
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
