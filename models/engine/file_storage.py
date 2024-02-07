import json
from models.base_model import BaseModel

 

class FileStorage:
    """this class manager storage of hbnb models in JSON"""
    __objects = {}  # This dictionary stores all objects

    def all(self, KL=None):
        """Return a dictionary of models currently in storage __objects."""
        if KL is not None:
            new_dict = {}
            for w, o in self.__objects.items():
                if isinstance(o, KL):
                    new_dict[w] = o
            return new_dict
        return self.__objects
    
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
    for w, o in self.__objects.items():
            elk_objects =[w] = o.to_dict()
    with open(self.__file_path, 'w') as fl:
        json.dump(elk_objects, fl)

def reload(self):
    """deserialize the JSON fl to __objects."""
    try:
        with open(self.__file_path, 'r') as fl:
            ow = json.load(fl)
            for w, o in ow.items():
                class_name = o.get("__class__", None)
                if class_name:
                    del o["__class__"]
                    self.__objects[w] = eval(class_name)(**o)
    except:
        pass       
