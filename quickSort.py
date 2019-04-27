c = 0
numbers = []
with open(r'C:\users\skbha\videos\QuickSort.txt', 'r') as f:
    for line in f.readlines():
        numbers.append(int(line[:-1]))
arr = numbers


def partition(l, r, array=arr):
    global c
    c += abs(l - r)
    i = l + 1
    len = abs(l - r) + 1
    if len % 2 == 0:
        idx = l + len / 2 - 1
    else:
        idx = l + (len - 1) / 2
    idx = int(idx)
    first = arr[l]
    middle = arr[idx]
    last = arr[r]
    s = sorted([first, middle, last])
    print("s", s)
    if s[1] == first:
        median = l
    if s[1] == middle:
        median = idx
    elif s[1] == last:
        median = r
    arr[l], arr[median] = arr[median], arr[l]
    pivot = array[l]
    for j in range(l + 1, r + 1):
        if array[j] > pivot:
            pass
        else:

            array[i], array[j] = array[j], array[i]
            i += 1
    array[i - 1], array[l] = array[l], array[i - 1]
    return i - 1


def call_left_subroutine(left, right):
    global c
    quick_sort(left, right)


def call_right_subroutine(left, right):
    global c

    quick_sort(left, right)


def quick_sort(left, right, array=arr):
    if left == right:
        return None
    else:
        global c
        pivot = partition(left, right)
        if pivot != left:
            call_left_subroutine(left, pivot - 1)
        if pivot != right:
            call_right_subroutine(pivot + 1, right)


print("original", arr)
quick_sort(0, len(arr) - 1)
print("quick_sorted", arr)
print("comparisions", c)
