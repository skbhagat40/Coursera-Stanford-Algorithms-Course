# For Lists/Looping

# iterating through two lists
# m1
from collections import defaultdict, ChainMap

list_a = ['a', 'b', 'c']
list_b = [1, 2, 3, 4]

for i in range(min(len(list_a), len(list_b))):
    print(list_a[i], list_b[i])

# better way of doing this is using zip.

for a, b in zip(list_a, list_b):
    print(a, b)


# Both give the same output.

# Iterating until a sentinal value
class Iterable:
    def __init__(self):
        self.i = 0

    def __call__(self, *args, **kwargs):
        self.i += 1
        return self.i


iter_obj = Iterable()

for el in iter(iter_obj, 3):
    print(el)

"""
we get the following output
1
2
"""


# So, the basic idea behind the iter method is that it takes a callable and
# it calls that callable until some sentinal value.

# It is basically a short-hand for the object based implementation where we
# have to implement __iter__ (mostly returns self) and __next__ methods.

# for else looping

def for_else():
    for el in [1, 2, 3]:
        if el == 4:
            print("got 4")
    else:
        print("unable to get 4")


for_else()
# prints 'unable to get 4'

# DICTIONARIES

# creating dictionaries using zip

my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(my_dict)
# {'a': 1, 'b': 2, 'c': 3}

# usage of default dict and set default

# counting occurances of words

words = ['shailesh', 'sam', 'aman', 'rajesh']

counts_dict = {}

for word in words:
    counts_dict.setdefault(word[0], 0)
    counts_dict[word[0]] += 1

# other way
print(counts_dict)
counts_dict = {}
for word in words:
    counts_dict[word[0]] = counts_dict.get(word[0], 0) + 1

print(counts_dict)
# yet another way
counts_dict = {}
counts_dict = defaultdict(int)
for word in words:
    counts_dict[word[0]] = counts_dict[word[0]] + 1

print(counts_dict)

# using chainmap

d = {'a': 1, 'b': 2}
d1 = {'a': 11, 'b': 22}
d2 = {'a': 33, 'c': 44}

print("chain map is")
print(ChainMap(d, d1, d2))

# List comprehension and generator expressions.

a = (el for el in range(4))  # creates a generator

print(a)

# Output: <generator object <genexpr> at 0x100b449d0>

# python popitem
