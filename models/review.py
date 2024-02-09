#!/usr/bin/python3
"""Definning the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Definning a class Review that inherits from the BaseModel."""

    place_id = ""
    user_id = ""
    text = ""
