"""
We will look at the concept of context managers in python.
context managers are used to define setup and tear down action.
They make use of yield statements for the transfer of control.
we will look at using @contextmanager for creating context managers.
"""

# Example 1. Opening a file

# without context manager

try:
    f = open('somefile.txt', 'w')
    f.write('Hello World \n')
finally:
    f.close()

# with using context managers

with open('somefile.txt', 'a') as f:
    f.write('Hello World Again!')

# Example 2. Using Locks

# without context managers
import threading

try:
    lock = threading.Lock()
    lock.acquire()
    print('do something')
finally:
    lock.release() # this is an important step. If we don't do this puppies die!

#using context managers

with lock:
    print('do something') # It's safe and puppies won't die!!

# writing your own context manager
from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

# checking file if exits before reading

try:
    f = open('somefile.txt', 'r')
    f.read()
except OSError:
    f.close()

# using context managers

with ignored(OSError):
    f = open('somefile', 'r')
    f.read()

# redirecting statndard output to a file

#without context managers
import sys

old_stdout = sys.stdout
with open('somefile.txt', 'w') as f:
    sys.stdout = f
    help(print)
sys.stdout = old_stdout

# using context-manager

@contextmanager
def redirect_outptut(sysobj):
    old_stdout = sys.stdout
    sys.stdout = sysobj
    yield sysobj
    sys.stdout = old_stdout

with open('somefile.txt', 'w') as f:
    with redirect_outptut(f):
        help(list)

"""
So we are able to see how context managers work.
on entering context it is called.
And it is also called while leaving the context.
"""
# let's write our own context manager which will create a file if it not exists and return it's handle
from contextlib import contextmanager
import os

@contextmanager
def mod_open(file_obj):
    try:
        f = open(file_obj, 'r')
        yield f
    except:
        os.system('touch {}'.format(file_obj))
        f = open(file_obj, 'r')
        yield f
        

# lets try it

with mod_open('unknown.txt') as f:
    print('f', f)
    print(f.read())