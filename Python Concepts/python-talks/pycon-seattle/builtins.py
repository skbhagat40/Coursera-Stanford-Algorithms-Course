# from builtins import __build_class__
import builtins

# from builtins import
old_bc = builtins.__build_class__


class Library(object):
    def foo(self):
        self.bar()
        print("I am Library method foo")


def new_build_class(func, name, base=None, *args, **kwargs):
    # if base == 'Library':
    #     print("base", base)
    # print("*" * 20)
    print("tapping into class creation")
    print("build args are function {}, name {}, args {}, kwargs {}".format(func, name, args, kwargs))
    # print(hasattr(name, 'bar'))
    if base is not None:
        print("base" * 10, base)
        if base == Library:
            print("**" * 10)
            print("Check if bar is defined or not")
            print(hasattr(name, 'bar'))
        return old_bc(func, name, base, *args, **kwargs)
    return old_bc(func, name, *args, **kwargs)


builtins.__build_class__ = new_build_class

"""
We get the following output for the build class


********************
tapping into class creation
build args are function <function Library at 0x105b63680>, name Library, args (<class 'object'>,), kwargs {}
********************
tapping into class creation
build args are function <function Client at 0x105b63680>, name Client, args (<class '__main__.Library'>,), kwargs {}
I am client code bar
I am Library method foo
********************
tapping into class creation
build args are function <function A at 0x105b63680>, name A, args (), kwargs {}
********************
tapping into class creation
build args are function <function B at 0x105b63680>, name B, args (<class '__main__.A'>,), kwargs {}
********************
tapping into class creation
build args are function <function C at 0x105b63680>, name C, args (<class '__main__.B'>,), kwargs {}
********************
tapping into class creation
build args are function <function A1 at 0x105b63680>, name A1, args (), kwargs {}
********************

"""


# globals()[__build_class__] = new_build_class
# print("globals", globals())


class Client(Library):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        try:
            hasattr(self, 'foo')
        except Exception as e:
            raise TypeError("Library code must implement foo method {}".format(e))

    def bar(self):
        print("I am client code bar")


c = Client()
c.foo()


# so it works. Now how can we enforce constraint on client code to implement bar.
# Let's hook into class creation using data model method.

# MRO in python

class A:
    pass


class B(A):
    pass


class C(B):
    pass


class A1:
    pass


class Test(C, A1):
    pass


t = Test()
# print(Test.__mro__)


# In python builtin module has a __build_class__ which we can hook into for class creation.
# How to find out
"""
import inspect
import builtins
inspect.getmembers(builtins)
"""

# Let's try to hook into python's class creation

# Another illustration of python being a protocol oriented language.
