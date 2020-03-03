# partial takes a function and returns a function with fewer arguments
# somewhat similiar to closures.
from functools import partial


def add(a, b):
    return a + b


add_2 = partial(add, 2)
assert add_2(4) == 6  # it works!
