"""entry point of the command interpreter"""
import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State, 'Place': Place, 'Review': Review, 'City': City, 'Amenity': Amenity
    }

    def do_quit(self, com):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, arg):
        """Handles End Of File character.
        """
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, model):
        """Create a new instance of BaseModel
        """
        if not model:
            print("** class name missing **")
            return
        elif model not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[model]()
        storage.save()
        storage.reload()
        print(new_instance.id)

    def do_show(self, args):
        """Prints string representation of an instance
        based on the class name
        """
        new = args.partition(" ")
        model = new[0]
        id = new[2]

        if id and ' ' in id:
            id = id.partition(' ')[0]

        if not model:
            print("** class name missing **")
            return
        elif model not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return
        key = model + "." + id
        if key not in storage.all():
            print("no instance found")
        else:
            print(storage.all()[key])

    def do_destroy(self, args):
        """destroys an instance based on the class name and id
        """
        new = args.partition(" ")
        model = new[0]
        id = new[2]

        if id and ' ' in id:
            id = id.partition(' ')[0]

        if not model:
            print("** class name missing **")
            return
        elif model not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return
        key = model + "." + id
        if key not in storage.all():
            print("no instance found")
        else:
            del storage.all()[key]
            storage.save()
            print("** instance deleted **")

    def do_all(self, model):
        """  prints all the string representtion of all the instances
        """
        arr = []
        all = storage.all().items()
        if model:
            model = model.split(' ')[0]  # remove possible trailing args
            if model not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in all:
                if k.split('.')[0] == model:
                    arr.append(str(v))
        else:
            for k, v in all:
                arr.append(str(v))

        print(arr)

    def do_update(self, args):
        """updating an instance with an attribute
        """
        new = args.partition(" ")
        model = new[0]
        next = new[2].partition(" ")
        id = next[0]
        next = next[2].partition(" ")
        attribute = next[0]
        next = next[2].partition(" ")
        value = next[0]

        if id and ' ' in id:
            id = id.partition(' ')[0]

        if not model:
            print("** class name missing **")
            return
        elif model not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif not id:
            print("** instance id missing **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return
        key = model + "." + id
        if key not in storage.all():
            print("no instance found")
            return

        if value[0] == '"':
            value = value.replace('"', '')
        elif value.find('.') > 0:
            try:
                value = float(value)
            except ValueError:
                pass
        else:
            try:
                value = int(value)
            except ValueError:
                pass

        setattr(storage.all()[key], attribute, value)
        storage.save()
        storage.reload()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
