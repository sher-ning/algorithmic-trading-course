
"""
global variable
accessible within both outer scope and within function
module scope spans a single file only e.g. main.py
"""

a = 25


def my_func():
    # lexical scope
    prefix = "value of 'a' is"
    print(f"{prefix} {a}")
    # a = 10 -> this will throw an exception, see scope below
    # at compile time, 'a' is already created, but not assigned


my_func()


"""
build in scope - top
global scope - main.py
local scope - def my_func

python will start from local to build-in, 
once the address of the object is found,
it will stop searching.

if you define your own print function, the print() will be override
"""

# access global score variables
print(globals()['a'])
print(globals()['my_func'])
