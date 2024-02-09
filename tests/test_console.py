#!/usr/bin/python3
'''
    Test cases for the console file
'''
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """preparing the testing environment"""
    def setUp(self):
        """setUp"""
        self.backup = sys.stdout
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """tearDown"""
        sys.stdout = self.backup

    def create_console(self):
        """the console"""
        return HBNBCommand()


class Test_Emptyline_Cmd(unittest.TestCase):
    """ Test emptyline command"""
    def setUp(self):
        self.console = HBNBCommand()

    def test_emptyline_cmd(self):
        """Test emptyline command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.emptyline()
            self.assertEqual("", output.getvalue())


class Test_Help_Cmd(unittest.TestCase):
    """Test help command"""
    def test_help_cmd(self):
        """Test help command"""
        console = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(console.onecmd("help"))
            self.assertIn("Documented commands", output.getvalue())


class Test_Quit_Program_cmds(unittest.TestCase):
    def test_quit_cmd(self):
        """Test quit command"""
        console = self.create_console()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_cmd(self):
        """Test EOF command"""
        console = self.create_console()
        self.assertTrue(console.onecmd("EOF"))


class TestCreateCmd(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_create_class_name_missing(self):
        """Test that try to create a class with a missing name """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_create_invalid_class_name(self):
        """Test that try to create a Class with invalid name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("create 134"))
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_create_user_instance(self):
        """Test that try to create a User instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create User")
            self.assertIn("User", output.getvalue())

    def test_create_nonexistent_class(self):
        """Test that try to create a nonexistent class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create Wissal")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())


class TestShowCmd(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_show_cmd_class_name_missing(self):
        """Test that try to show a missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual("** class name missing **\n", output.getvalue())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd(".show()"))
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_show_cmd_invalid_class_name(self):
        """Test that try to show an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show Oumaima")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_show_cmd_instance_id_missing(self):
        """Test that try to show a missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_show_cmd_no_instance_found(self):
        """Test that try to show a non instance found"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("show User 19960429")
            self.assertEqual("** no instance found **\n", output.getvalue())


class TestDestroyCmd(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_destroy_cmd_missing_class_name(self):
        """Test destroy command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_destroy_cmd_invalid_class_name(self):
        """Test destroying an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("destroy wissal"))
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_destroy_cmd_missing_instance_id(self):
        """Test destroying a missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("destroy User"))
            self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_destroy_cmd_instance_not_found(self):
        """Test destroying a none existing instance"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("destroy User 19960429"))
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_destroy_cmd_success(self):
        """Test destroy cmd successfully"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create User")
            user_id = output.getvalue().strip()
            self.assertTrue(user_id)

            self.console.onecmd(f"destroy User {user_id}")
            self.assertEqual("", output.getvalue().strip())


class TestAllCmd(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_all_cmd_with_no_args(self):
        """Test all cmd with no arguments provided """
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all")
            self.assertIn("BaseModel", output.getvalue())

    def test_all_cmd_with_aclass_name(self):
        """Test all cmd with a valid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all User")
            self.assertNotEqual("", output.getvalue().strip())

    def test_all_cmd_with_invalid_class_name(self):
        """Test all cmd with an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all Wissal")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_all_cmd_with_invalid_args(self):
        """Test all cmd with an invalid arguments"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("all User 1996")
            self.assertEqual("** no instance found **\n", output.getvalue())


class TestUpdateCmd(unittest.TestCase):
    def setUp(self):
        """Test update command"""
        self.console = HBNBCommand()

    def test_update_cmd_missing_class_name(self):
        """Test update with a missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual("** class name missing **\n", output.getvalue())

    def test_update_cmd_invalid_class_name(self):
        """Test update command with an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update Wissal"))
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

    def test_update_cmd_missing_instance_id(self):
        """Test update command with missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update User"))
            self.assertEqual("** instance id missing **\n", output.getvalue())

    def test_update_cmd_instance_not_found(self):
        """Test update command with instance is not found"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update User 199604"))
            self.assertEqual("** no instance found **\n", output.getvalue())

    def test_update_cmd_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update User 123456"))
            self.assertEqual("** attribute name missing **\n",
                             output.getvalue())

    def test_update_cmd_missing_attribute_value(self):
        """Test update command with missing attribute value"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(self.console.onecmd("update User 1996046 Wissal"))
            self.assertEqual("** value missing **\n", output.getvalue())

    def test_update_cmd_success(self):
        """Test update command successfully"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("create User")
            user_id = output.getvalue().strip()
            self.assertTrue(user_id)

            self.console.onecmd(f"update User {user_id} name 'Leknouch'")
            self.assertEqual("", output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
