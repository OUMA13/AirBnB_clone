#!/usr/bin/python3
""" this Module is for definning the HBNB Console """
import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ 
    this is the Class for AirBnB clone command interpreter
    using hbnb as a prompt
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ End of file Command to exit the program (Ctrl+D) """
        print("")
        return True

    def do_quit(self, line):
        """ this is the quit command to exit the program """
        return True
    
    def emptyline(self):
         """ Do nothing when receiving an empty line """
         pass
    
    def do_create(self, arg):
        """ 
        Creates a new instance of a class BaseModel
        and print the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
    
        try:
            owclass_name = args[0]
            own_instance = eval(owclass_name)()
            own_instance.save()
            print(own_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based on id and class name givem as arguments
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        owclass_name = args[0]
        try:
            cls = eval(owclass_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        storage = FileStorage()
        storage.reload()
        owobj_dict = storage.all()
        ow_instance_id = args[1]
        ow_key = "{}.{}".format(owclass_name, ow_instance_id)
        if ow_key in owobj_dict:
            print(owobj_dict[ow_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        owclass_name = args[0]
        try:
            cls = eval(owclass_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        storage = FileStorage()
        storage.reload()
        owobj_dict = storage.all()

        ow_instance_id = args[1]
        ow_key = "{}.{}".format(owclass_name, ow_instance_id)
        if ow_key in owobj_dict:
            del owobj_dict[ow_key]
            storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """

        if args:
            try:
                cls = eval(args)
                storage = FileStorage()
                storage.reload()
                print([str(obj) for obj in storage.all().values() if isinstance(obj, cls)])
            except NameError:
                print("** class doesn't exist **")
                return
        else:
            storage = FileStorage()
            storage.reload()
            objects = storage.all()
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        ow_key = "{}.{}".format(args[0], args[1])
        storage = FileStorage()
        storage.reload()
        owobj_dict = storage.all()
        if ow_key not in owobj_dict:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(owobj_dict[ow_key], args[2], args[3])
        storage.save()

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()