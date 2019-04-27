# python example to demonstrate decorators
'''decorators act as gift wrappers they added extra functionality to existing functions'''

def make_pretty(func):
    def inner_func():
        print("i am inside a decorator gift wrapper")
        func()
    return inner_func
@make_pretty
def original():
    print("i am original")
original()

def universal_decorator(func):
    def inner(*args,**kwargs):
        print("i am universal decorator")
        return func(*args,**kwargs)
    return inner
# properties in python
# man = Man()
# man.temp is same is man.__dict__.get(temp)
# property is used to modify object access in python oop environment
# to prevent users from modiying the variables and posting unwanted values. Let's do and example
# one obvious way is to use getters and setters , but that involves re-writing code. Simple way to avoid that is using property. A property is a property object that facilitates acces to a private variable. Let's see!
class Temprature(object):
    def __init__(self,temp=0):
        self.temp = temp
    def set_temp(self,value):
        print("setting temprature")
        self._temp = value
    def get_temp(self):
        print("getting temprature")
        return self._temp
    temp = property(fget=get_temp,fset=set_temp)
# let's see it in action
t1 = Temprature()
t1.temp = 44 # this should print setting temp
print(t1.temp) # this should print getting temp
# another way of implementing this using decorators
# fset and fget can also be set using getter attribtes
'''For example ,
temp = property(get_temp,set_temp) is equivalent to 
temp = property # property object
temp = temp.getter(get_temp)
temp = temp.setter(set_temp)'''
class Tempraturep(object):
    def __init__(self,temp=0):
        self.temp = temp
    @property
    def temp(self):
        print("i am property getter")
        return self._temp
    @temp.setter
    def temp(self,value):
        print("i am property setter")
        self._temp = value
# so basically what property does is provide access to private variable _temp
t = Tempraturep()
t.temp = 40
print('temp is ',t.temp)