#!/usr/bin/python3
"""Contains the TestCityDocs classes."""

from models.base_model import BaseModel
import json
import BaseModel

class City(BaseModel):
    """ Contains the TestCityDocs classes"""

    state_id = ""
    name = ""

ow_city = City()
ow_city.name = "casa"
ow_city.state_id = "MA"
ow_city.save()
print(ow_city.to_dict())
wnw_city = City.from_dict(ow_city.to_dict())
print(wnw_city.name)
print(wnw_city.state_id)
