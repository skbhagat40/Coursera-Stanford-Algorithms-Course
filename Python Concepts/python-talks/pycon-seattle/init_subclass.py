class Base:
    def __init_subclass__(cls, foo=None, **kwargs):
        print("tapping into init subclass")
        print("arguments are")
        print(cls, foo, kwargs)
        return super().__init_subclass__(**kwargs)


class Derived(Base):
    def foo(self):
        print('foo')


client = Derived()

"""
We get the following output 

tapping into init subclass
arguments are
<class '__main__.Derived'> {}

"""
