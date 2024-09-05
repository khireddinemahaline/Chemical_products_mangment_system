#!/usr/bin/env python3
"""consle.py
----to start the file : ./console.py"""
from models import storage
from models.base_model import BaseModel
from models.users import User
from models.products import Product 
from models.orders import Order
from models.order_status import Order_status
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb)"

    def do_create(self, args):
        """Command to create a new instance of BaseModel
        usage: create <class_name>"""
        
        if not args:
            print("** class name missing **")
            return

        args = args.split(' ')
        if len(args) < 1:
            print("** class name missing **")
            return
        
        class_name = args[0]
        params = args[1:]
        new_obj = {}
        
        for param in params:
            try:
                key, value = param.split('=', 1)
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ')
                elif value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif '.' in value:
                    value = float(value)
                else:
                    value = int(value)
                new_obj[key] = value

                
            except ValueError:
                print(f"** invalid value for {key} **")
                return
            except Exception as e:
                print(f"** error parsing parameter: {param} **")
                print(e)
                return
            

        if class_name in globals():
            model_class = globals()[class_name]
            model = model_class(**new_obj)
            model.save()
            print(model.id)

            if class_name == 'Order':
                try:
                    # Automatically create the associated OrderStatus entry
                    order_status = Order_status(order_id=model.id)
                    order_status.save()
                except Exception as e:
                    print(f"** error creating OrderStatus: {e} **")
                    # Optionally, you could also delete the created Order if the OrderStatus creation fails
                    model.delete()
                    return
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """string representation based on the class name and id"""
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            keyU = arg[0] + '.' + str(arg[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, args):
        """Destroy an instance"""
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            keyU = arg[0] + '.' + str(arg[1])
            if keyU in dic:
                del dic[keyU]
                models.storage.save()
            else:
                print("** no instance found **")
        return

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        """show all instance"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in models.classes:
                print("** class doesn't exist **")
                return
            print('i am in the args')
            for k, v in storage.all(args).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                # i removed the "args" from this line
                print_list.append(str(v))
        print(print_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        elif arg[0] not in models.classes:
            print("** class doesn't exist **")
            return
        key = arg[0] + '.' + arg[1]
        dic = models.storage.all()
        try:
            obj = dic[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            ins_one = type(getattr(obj, arg[2]))
            arg[3] == ins_one(arg[3])
        except AttributeError:
            pass
        setattr(obj, arg[2], arg[3])
        models.storage.save()
        return

    def do_quit(self, arg):
        """quit"""
        return True

    def do_EOF(self, args):
        """handel EOF"""
        return True

    def emptyline(self):
        """No action"""
        pass


if __name__ == '__main__':
    """HBNBCommand()"""
    HBNBCommand().cmdloop()
