import importlib

import new_module
import types
import socket, math
import sys
from pprint import pprint

# importing new_module will execute new_module line by line
# a module is also an object in python

print(globals()['new_module'])
# "<module 'new_module'>"

# proves that module is an object in memory
print(type(new_module))
print(isinstance(new_module, types.ModuleType))
print(hex(id(new_module)))

my_mod = new_module
# same address in memory
print(hex(id(my_mod)))

# list of PyObjects/Attributes in New_Module
# after importing new_module, module object attributes available
print(dir(new_module))

# __name__ -> new module
print(new_module.__dict__['__name__'])
print(new_module.__name__)  # made simpler
print(new_module.__file__)  # file path

new_module.__dict__['my_func']()  # you can invoke function object


print(globals()['math'])
print(globals()['socket'])


# finder and loader
pprint(sys.meta_path)
importer = sys.meta_path[2]

# spec = importer.find_spec('itertools')
pprint(sys.modules)  # prints all pre-loaded module


del socket
print('socket' in globals())  # false
print('socket' in sys.modules)  # true

# another way of importing module instead of import
import_me = importlib.import_module('import_me')
print(globals()['import_me'])
import_me.hola()

# from math import ...
# python does not do partial loading, it will load everything in that module

# __main__ is the execution entry point

# package is a directory or folder of modules
# module is a single file

# package has path
import collections
print(collections.__path__)
# print(socket.__path__) -> undefined

# regular packages
# __init__.py -> package
# will be executed automatically like a constructor call()
print(collections.__file__)

# print the __init__.py path

# importing package does not import modules inside
# import collections.mod1 -> import module inside package

# absolute import means pack1.pack2.mod2 -> outer to inner

# from . import mod2 -> current directory
# from .. import mod2 -> parent directory
# can only be used inside packages -> contain __init__

# _x prefix with _ will not be exported

# __all__ ["y", "method name"] -> will be exported

