
class Bicycle:

    age = 1

    def __init__(self):
        self._gear = 1
        self._speed = 5


class MyClass:

    # create a reference to the instance
    @classmethod  # becomes a static method
    def say_hello(cls):
        print(f"Hello {cls}")


obj = MyClass()
print(MyClass.say_hello)

# method and obj are at the same address
print(obj.say_hello)
print(hex(id(obj)))

# print(obj.say_hello())
print(MyClass.say_hello)
