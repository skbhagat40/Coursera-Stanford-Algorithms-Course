class BaseMeta(type):
    def __new__(cls, *args, **kwargs):
        print('hook to tap into instantiation of classes derived from base')
        print('arguments are')
        print(cls, args, kwargs)
        return super().__new__(cls, *args, **kwargs)


class Base(metaclass=BaseMeta):
    def bar(self):
        print("i am base class bar")
        return self.foo()


class Derived(Base):
    def foo(self):
        print("foo")


client = Derived()
"""
After running the above code we get the following output -


hook to tap into instantiation of classes derived from base
arguments are
<class '__main__.BaseMeta'> ('Base', (), {'__module__': '__main__', '__qualname__': 'Base', 'bar': <function Base.bar at 0x1018860e0>}) {}
hook to tap into instantiation of classes derived from base
arguments are
<class '__main__.BaseMeta'> ('Derived', (<class '__main__.Base'>,), {'__module__': '__main__', '__qualname__': 'Derived', 'foo': <function Derived.foo at 0x1018864d0>}) {}

"""
# thus we can see all the attributes the derived class has.
