"""A python program that implements dutch national flag algorithm i.e sorts the arrays of 0s, 1s and 2s in single pass and
using constant space.
The algorithm which I am going to implement works as follows -
1. It makes use of three pointers namely 0's pointer, 1's pointer and Traversing pointer which traverses through the array.
2. So, Whenever we encounter 0 we add it to the start of the array.
3. Whenever we encounter a one we swap it with the element next to it and move forward the 1's pointer.
I guess this is it. And it's making use of two pointers only. Somewhat similar to pivotization in randomized quick sort algorithm."""
from collections import Counter

array = [2, 0, 2, 1, 1, 0]


# def sort_array(arr):
#     one_ptr = 0
#     # here idx behaves as the traversor.
#     for idx,el in enumerate(arr):
#         if el == 0:
#             del arr[idx]
#             arr.insert(0, el)
#             if idx != 0 and one_ptr != 0:
#                 one_ptr += 1
#         if el == 1:
#             # swap with forward element and move the traversor and move the one's pointer
#             print("swapping", one_ptr, idx, arr[one_ptr], arr[idx])
#             arr[one_ptr], arr[idx] = arr[idx], arr[one_ptr]
#             one_ptr += 1
#         if el == 2:
#             # do nothing just move forward
#             continue
#         print("current state of the array", arr)
#         print("current one pointer", one_ptr)
#     return arr
#
#
# print("result of sorting is ", sort_array(array))

# def sort_array_v2(array):
#     ones_start = 0
#     ones_end = 0
#     ctr = 0
#     while ctr < len(array):
#         if array[ctr] ==

def pivotize(array):
    pivot_ctr = 0
    pivot = array[pivot_ctr]
    traverser = 1
    left_ctr = None
    while traverser < len(array):
        print("traverser", traverser)
        if array[traverser] > pivot:
            traverser += 1
        elif array[traverser] < pivot:
            print(len(array), traverser, pivot_ctr)
            print("shifting", array[pivot_ctr + 1], array[traverser], "array at this point",array)
            array[pivot_ctr + 1], array[traverser] = array[traverser], array[pivot_ctr + 1]
            print("array after shifting", array)
            print("=="*5,left_ctr)
            if left_ctr is not None:
                # print("=="*10)
                array[left_ctr], array[pivot_ctr + 1] = array[pivot_ctr + 1], array[left_ctr]
                left_ctr += 1
            else:
                array[pivot_ctr], array[pivot_ctr + 1] = array[pivot_ctr + 1], array[pivot_ctr]
            pivot_ctr += 1
            traverser += 1
        elif array[traverser] == pivot:
            print("equal case")
            print("array before equal case", array)
            array[pivot_ctr + 1], array[traverser] = array[traverser], array[pivot_ctr + 1]
            print("array after", array,"pivot ctr and it's value", pivot_ctr, array[pivot_ctr])
            if left_ctr is None:
                left_ctr = pivot_ctr
            pivot_ctr += 1
            traverser += 1
    print("result of pivotize is", array)


#arr = [1, 6, 5, 11, 11, 4, 1, 23, 7, 9, 6, 3, 4, 8, 10, 5, 0, 4, 11]
#arr = [1,1,0,0,0,0,2,2,2,2,2,1,0,1,1,1,2]
arr = [2,0,2,1,1,0]
print(pivotize(arr[:]))
print("count vals",Counter(arr))
