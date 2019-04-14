def merge(arr1, arr2):
    print(arr1, arr2)
    leftCtr = 0
    rightCtr = 0
    merged = []
    while leftCtr < len(arr1) and rightCtr < len(arr2):
        if arr1[leftCtr] < arr2[rightCtr]:
            merged.append(arr1[leftCtr])
            leftCtr += 1
        else:
            merged.append(arr2[rightCtr])
            rightCtr += 1

    merged.extend(arr1[leftCtr:])
    merged.extend(arr2[rightCtr:])

    return merged


def mere_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
    r1 = mere_sort(left)
    r2 = mere_sort(right)
    res = merge(r1, r2)
    return res


arr = [5, 3, 1, 2, 1, 5, 3, 3, 5, 9, 11]
res = mere_sort(arr)
print("result", res)
print("original array is {} and sorted array is {} ".format(arr, res))
