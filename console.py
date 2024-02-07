#!/usr/bin/python3
""" this Module is for definning the HBNB Console """
import cmd
import json
from models.base_model import BaseModel

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
    """Creates a new instance of a class"""
    args = arg.split()
    if len(args) == 0:
        print("** class name missing **")
        return
    
 
    try:
        class_name = args[0]
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)
    except NameError:
        print("** class doesn't exist **")


def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        class_name = args[0]
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instances = cls.load_from_file()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        class_name = args[0]
        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instances = cls.load_from_file()
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            del instances[key]
            BaseModel.save_to_file(instances)
        else:
            print("** no instance found **")
    
def do_all(self, arg):
        """Prints all string representation of all instances"""
        instances = BaseModel.load_from_file()
        args = arg.split()
        if len(args) == 0:
            print([str(instance) for instance in instances.values()])
            return
        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        #The first snippet checks if the class name in the key matches the provided arg
        print([str(instance) for key, instance in instances.items() 
               if key.split('.')[0] == arg])
        

def do_update(self, arg):
        """Updates an instance based on the class name and id"""
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
        instances = BaseModel.load_from_file()
        key = "{}.{}".format(args[0], args[1])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(instances[key], args[2], args[3])
        BaseModel.save_to_file(instances)
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()