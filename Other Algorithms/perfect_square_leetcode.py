def find_perfect_square_or_not(num):
    list_array = list(range(num//2 + 1))


def binary_search(num):
    list_arr = range(num//2 + 2)
    low = 0
    high = len(list_arr)-1
    mid = (high + low)//2
    flag = False
    while low<=high:
        if list_arr[mid]*list_arr[mid] < num:
            low = mid + 1
        if list_arr[mid]*list_arr[mid] > num:
            high = high -1
        if list_arr[mid]*list_arr[mid] == num:
            flag = True
        if flag:
            return list_arr[mid]
        else:
            mid = (high + low)//2

print(binary_search(2147483647))