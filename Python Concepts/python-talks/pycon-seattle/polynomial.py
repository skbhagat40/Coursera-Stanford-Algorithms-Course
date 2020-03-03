class Polynomial(object):
    def __init__(self, *args):
        self.coefficients = args

    def __str__(self):
        return ",".join(str(x) for x in self.coefficients)

    def __add__(self, other):
        return Polynomial(
            *[x + y for x, y in zip(self.coefficients, other.coefficients)])  # tuple unpacking sort of thing.


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 5)

print(p1 + p2)  # output is 4,6,8

# Here we are using __add__ hook/data model method and overriding it.
# Almost everything in python has a hook which you can use.
# There is a hook for overriding class creation using builtins.
