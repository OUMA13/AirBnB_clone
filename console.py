#!/usr/bin/python3
""" this Module is for definning the HBNB Console """
import cmd

class HBNBCommand(cmd.Cmd):
    """ 
    this is the Class for AirBnB clone command interpreter
    using hbnb as a prompt
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ End of file Command to exit the program """
        print("")
        return True

    def do_quit(self, line):
        """ this is the quit command to exit the program """
        return True
    
    def emptyline(self):
         """ this to do nothing when receiving an empty line """
         pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
   
