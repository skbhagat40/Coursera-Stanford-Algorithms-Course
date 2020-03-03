from datetime import datetime


def time_it(func):
    def f(*args, **kwargs):
        start = datetime.now()
        rv = func(*args, **kwargs)
        end = datetime.now()
        print(start - end)
        return rv

    return f


@time_it
def add(a, b):
    return a + b


@time_it
def sub(a, b):
    return a - b


print(add(2, 3))

# suppose we want to time these operations, then we can do

# The inefficient way of doing the same thing would be

start = datetime.now()
add(1, 2)
end = datetime.now()

start = datetime.now()
add(1, 2)
end = datetime.now()

# same for sub


