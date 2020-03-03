def add(a, b):
    return a + b


class Adder:
    def __call__(self, *args, **kwargs):
        return sum(args)


print("add", add(1, 2))

add = Adder()

print("Adder", add(1, 2))

"""
We get the following output - 

add 3
Adder 3

Using a class has an added benefit of maintaining the state.
"""