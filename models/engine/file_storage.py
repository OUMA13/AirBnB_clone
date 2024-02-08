import json
import models
from models.user import User
 

class FileStorage:
    """this class manager storage of hbnb models in JSON"""
    __file_path = "file.json"
    __objects = {}


def all(self, cls=None):
    """Return a dictionary of models currently in storage __objects."""
    if cls is not None:
        new_dict = {}
        for ow_k, ow_v in self.__objects.items():
            if isinstance(ow_v, cls):
                new_dict[ow_k] = ow_v
        return new_dict
    return FileStorage.__objects
    
def new(self, obj):
    """Sets the object in the __objects dictionary with the key <obj_class_name>.id
    Adds a new object to the storage dictionary"""
    if obj is not None:
        wisso = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(wisso, obj.id)] = obj

def save(self):
    """Serialize __objects into a JSON file (path: __file_path)
To save the storage dictionary"""
    elk_objects = {}
    for ow_k, ow_v in self.__objects.items():
            elk_objects ={ow_k: ow_v.to_dict()}
    with open(FileStorage.__file_path, 'w') as fl:
        json.dump(elk_objects, fl)

def reload(self):
    """deserialize the JSON fl to __objects."""
    try:
        with open(FileStorage.__file_path, 'r') as fl:
            data = json.load(fl)
            for ow_k, ow_v in ow_k.items():
                class_name = ow_v.get("__class__", None)
                if class_name:
                    del ow_v["__class__"]
                    self.__objects[ow_k] = eval(class_name)(**ow_v)
    except FileNotFoundError:
        pass
    