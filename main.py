"""
all types in python are PyObject
variable r is stored on the heap in memory
"""
# <class 'ini'>
r = 10
print(type(r))

r = "rhino"
print(r)
print(type(r))

# List is a PyVarObject that store PyObjects
a = [1, 2, 3]
b = [1, 2, 3]

# equality check for each element in list -> true
print(a == b)

# equality check for memory address of list -> false
print(a is b)

# interning or re-using objects
# only one None object is created for lifetime of the program
y = None
x = None

# python caches some commonly used objects

# they have the same memory address on heap
print(x is y)

# the memory address in memory is the same
print(hex(id(x)))
print(hex(id(y)))

# same address on the heap
x = 42
y = 42
print(hex(id(x)))
print(hex(id(y)))
print(x is y)


def test():
    # same memory address as x and y
    g = 42
    h = 42
    print(hex(id(g)))
    print(hex(id(h)))


# test()

# strings work the same way
a = "some string"
b = "some string"
print(id(a))
print(id(b))
print(id("some string"))


# passing reference to function is different
def assign_new_list(arr):
    arr = [1, 2, 3]  # point to new object [1,2,3]
    # end of function, arr removed from scope


nums = [4, 5, 6]
assign_new_list(nums)
print(nums)


# default mutable parameters
# parameter my_list=[] is stored as a variable inside function object
def add_two_to_list(my_list=[]):
    # use list=None, and check if none to create new list
    my_list.append(2)
    return my_list


# function is also an object in python <class 'function'>
print(hex(id(add_two_to_list)))



