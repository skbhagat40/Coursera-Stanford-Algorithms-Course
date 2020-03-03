Talk Link -
This is a talk from pycon seattle.

Topics included in this talk -

1. Python as a protocol oriented language.

    For Every Higher level implementation in python there  is a corresponding data model method ( dunder method) which we can hook into and override.
    Example implementation in polynomials.py

2. Meta Classes in Python.
 Sort of a way for library code to enforce constraint on how user code is implemented.
    - a using builtins. A method to hook into class creation. see builtins.py
 Another way of enforcing constraint on how derived class are instantiated is using Meta Classes
 - Meta Classes are classes which inherit from type. Normal classes inherit from object.
 Example implementation in metaclasses.py.
 - Another was for library code to enforce control on client code is using __init_subclass__
 Example implementation in init_subclass.py

3. Decorators in python

    The idea behind decorators is that everything in python is a live piece of code.
    In python objects (i.e. functions also) can be constructed and modified at the runtime.
    Example Implementation in decorators.py

4. Generators in python

    First some demo implementation of how things work under the hood in python in demo_implementation.py.

    The idea behind the generators is that when you have some long computation you don't want for the entire computation to finish.
    Wastage of time and memory.

    Let's see an example in generator_ex.py

    The above implementation can be simplified even further.

    The core concept behind generators is the *transfer of control back and forth between user code and driver code*.

    This can be done using the yield keyword.

    Example implementation in yield_ex.py

5. Context Managers in python

    We use context managers when we have some setup action and teardown action.
    For example opening and closing a file.
    We can use __enter__ and __exit__ hooks to write our own custom context manager.
    Then we can combine it with generators for control the order of execution of enter and exit methods.
    We can also use contextmanager decorator.

    Example implementation in context_manager.py