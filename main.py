
# closure is a function with a free variable

def outer():
    a = 25
    name = "python"

    def inner(prefix):
        print(prefix, name)

    return inner


my_func = outer()

# the name variable is a free variable with a reference count
my_func("hi")


def counter(start):

    def increment(step=1):
        nonlocal start
        start += step
        print(start)

    return increment


my_func = counter(1)
# start is the free variable
my_func(1)
my_func(1)
my_func(1)
my_func(1)
my_func(1)
my_func(1)

