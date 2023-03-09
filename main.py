from bicycle import Bicycle

b = Bicycle()

# print(b.__dict__)

# mapping proxy object, read-only dictionary
# print(Bicycle.__dict__)

# == .__dict__
print(vars(Bicycle))
print(b.__dict__)

fields = {'a': 10, 'b': 20, 'c': 30}

# create and set fields dynamically to the object instance
for attr, value in fields.items():
    setattr(b, attr, value)

# this is not a read-only dictionary, can be assigned value directly
# print(b.__dict__)
