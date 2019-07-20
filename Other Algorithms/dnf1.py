"""Better Implementation of Dutch National Flag using three pointers low mid and high.
while mid <= high.
low keeps track of the boundary of zeroes.
mid keeps track of the boundary of the ones.
high keeps track of the starting of the twos."""

def sort012v1(array):
    low = 0
    mid = 0
    high = len(array) - 1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            mid += 1
            low += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
            # the current value of mid will be examined in the next iteration.
    print("the result of sorting is", array)
    return array

def sort012( a):
    lo = 0
    hi = len(a) - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid]
            hi = hi - 1
    return a

arr = [2,2,0,1,1,0,2,1,1,0]
print("result of sorting is", sort012(arr))
print("the result of sorting using prev function is", sort012v1(arr))