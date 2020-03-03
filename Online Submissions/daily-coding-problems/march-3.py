"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""
from functools import reduce


def check_sum(arr, k):
    arr_items = set(arr)
    for item in arr:
        if k - item in arr_items:
            return True


assert check_sum([10, 15, 3, 7], 17) == True
print(check_sum([10, 15, 3, 7], 17))

"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def replace_arr(arr):
    prod = reduce(lambda x, y: x * y, arr)
    return [prod // i for i in arr]


assert replace_arr([3, 2, 1]) == [2, 3, 6]

# can't use division
# maintain lett and right arrays
"""
Approach my maintaining left and right arrays.
"""


def replace_arr1(arr):
    left = [1] * (len(arr))
    right = [1] * (len(arr))
    prod = 1
    for idx, el in enumerate(arr):
        left[idx] = left[idx - 1] * el
    for idx, el in enumerate(reversed(arr)):
        right[idx] = right[idx - 1] * el
    right.reverse()
    right.append(1)
    del right[0]
    del left[-1]
    left.insert(0, 1)
    print("finally left is", left)
    print("finally right is", right)
    return [left[i] * right[i] for i in range(len(arr))]


print(replace_arr1([3, 2, 4, 6]))
print(replace_arr([3, 2, 4, 6]))

# Time complexity is O(n) in both cases.
