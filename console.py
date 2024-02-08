#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.task import Task
from models.group import Group
from models.time_tracker import TimeTracker

classes = {"User": User, "Task": Task, "BaseModel": BaseModel, "Group": Group,
           "TimeTracker": TimeTracker}

class TASKCommand(cmd.Cmd):
    """
    TASKCommand class for a simple command-line interpreter.
    
    Implements basic commands and a custom prompt for the TASK MANAGER console.
    """
    
    prompt = '(TASK) '
    
    def do_EOF(self, arg):
        """Exit the console program with ^C"""
        print()
        return True
    
    def do_quit(self, arg):
        """Exit console program with the keyword quit"""
        return True
    
    def do_emptyline(self):
        """Print nothing when line is empty"""
        pass
    
    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict
    
    def do_create(self, arg):
        """Creates a new instance of a specified class with given parameters and saves it.

        Command syntax: create <Class name> <param 1> <param 2> <param 3>...
        Param syntax: <key name>=<value>
        Value syntax:
        - String: "<value>" => starts with a double quote
        Any double quote inside the value must be escaped with a backslash \
        All underscores _ must be replaced by spaces
        Example: name="My_little_house"
        - Float: <unit>.<decimal> => contains a dot .
        - Integer: <number> => default case

        If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped.

        """
        try:
            if not arg:
                raise SyntaxError("** class name missing **")

            args = arg.split()
            class_names = args[0].split(',')

            for class_name in class_names:
                kwargs = {}
                class_args = args[1:]
                for arg in class_args:
                    key, _, value = arg.partition('=')
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                    else:
                        try:
                            value = eval(value)
                        except (NameError, SyntaxError):
                            pass
                    kwargs[key] = value

                if class_name not in globals():
                    print("** class doesn't exist **")
                    continue

                obj = globals()[class_name](**kwargs)
                obj.save()
                print("{}".format(obj.id))

        except SyntaxError as e:
            print(e)


        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)

                
    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
                
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).

        Usage: destroy <class_name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
                
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.

        Usage: all [class_name]
        """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")
    
    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating an attribute (save the change into the JSON file).

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2], args[3]

            key = "{}.{}".format(class_name, obj_id)
            all_objs = models.storage.all()

            if key not in all_objs:
                print("** no instance found **")
            elif attr_name == "id" or attr_name == "created_at" or attr_name == "updated_at":
                print("** cannot update id, created_at, or updated_at **")
            else:
                obj = all_objs[key]
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    try:
                        setattr(obj, attr_name, attr_type(attr_value))
                        obj.save()
                    except (ValueError, TypeError):
                        print(f"** invalid value for {attr_name} **")
                else:
                    print(f"** attribute {attr_name} not found in {class_name} **")


if __name__ == '__main__':
    """
    Entry point of the program. Creates an instance of TASKCommand and starts the command loop.
    """
    TASKCommand().cmdloop()
