# count inversions by piggybacking merge_sort
# accompolished in nlogn i guess!
def count_split_inversions(left, right):
    final = []
    left_ctr = 0
    right_ctr = 0
    split_inversions = 0
    while left_ctr < len(left) and right_ctr < len(right):
        if left[left_ctr] < right[right_ctr]:
            final.append(left[left_ctr])
            left_ctr += 1
        else:
            split_inversions += len(left)-left_ctr
            final.append(right[right_ctr])
            right_ctr += 1
    final.extend(left[left_ctr:])
    final.extend(right[right_ctr:])
    return split_inversions,final


def count_inversions(array):
    if len(array) == 1:
        return 0,array[:]
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left_inversions,left_sorted = count_inversions(left)
        right_inversions,right_sorted = count_inversions(right)
        split_inversions,sorted = count_split_inversions(left_sorted,right_sorted)
        return split_inversions+left_inversions+right_inversions,sorted

numbers = []
with open(r'C:\users\skbha\videos\assign.txt','r') as f:
    for line in f.readlines():
        numbers.append(int(line[:-1]))

print(count_inversions(numbers))
