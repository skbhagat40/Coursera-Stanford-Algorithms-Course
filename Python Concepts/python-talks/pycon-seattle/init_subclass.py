class Base:
    def __init_subclass__(cls, **kwargs):
        print("tapping into init subclass")
        print("arguments are")
        print(cls, kwargs)
        return super().__init_subclass__()


class Derived(Base):
    pass


client = Derived()

"""
We get the following output 

tapping into init subclass
arguments are
<class '__main__.Derived'> {}

"""
