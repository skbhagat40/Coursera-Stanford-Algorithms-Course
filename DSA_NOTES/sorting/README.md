Sorting - Having some order based on some property.

1. Selection Sort - 
    finding kth minimum in the array.
Observation - find 1st minimum in O(n) and then remove it. Time Complexity = O(kN)
Instead or removing(which takes O(n) ) we swap it with first index.

Time Complexity = O(n^2)
space = O(1)
no. of swaps = n
no. of comparisions = n^2
best case time complexity = O(n^2)

Stabilty - can make it stable by not taking index which is equal to min_val, and saperately handling the case of continuos values.

```
def selectionSort(arr):
    for i in range(len(arr)):
        min_index = -1
        min_val = INT_MAX
        for j in range(i,len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
            # this is somewhat similiar to temp and break , two pointer problem.
        arr[i], arr[min_index] = arr[min_index], arr[i]
```

2. Bubble Sort - Sort the queue of persons without breaking it.

Observation - Compare each element with it's neighbor and swap if it is greater.
Stability - if equal we don't swap. -(this will make it stable.)

best case time complexity = O(N) break if no swaps are required.
no. of swaps = n2
no. of comparisions = n2
space = 1

```
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```

3. Insertion Sort = Sorting Cards.

Observation = Keep the left part of the array sorted. compare and shift till we are finding bigger elements.
Need to create a void (temp) and keep shifting.

best case tc = O(n) - no. need to do any optimization.
stop when lesser found.
comp = n2
swaps = n2
stability = if we break loop on less than or equal , then it will be stable.

```
def insertionSort(arr):
    for i in range(len(arr)):
        temp = a[i]
        start = i-1
        while a[start] > temp:
            swap
```

4. Create a wave. given an array . arrange the elements such that, a[i] > a[i+1] < a[i+2]

Whenever there is a graphical question, try to think in terms of graph. Same as in case of binary search over answer space questions.

Observation - swap (odd indices) with previous element if it is greater than the previous one and then move two places. 

sort, skip two places and swap.

Lexicographically Sorted - sort the array and swap pair-wise.

Sorting II

5. The Quick Sort Algorithm - 

Observation -  We have a pivot, partition the array on two halves based on the pivot.
The pivot will end up at its correct position. And everytime we are dividing the problem in half. We do this till we are left with single element in the array.
An Example of divide and conquer algo.

Pseudocode for the algo- (recursive algo.)

```
def quickSort(arr,start_idx, end_idx):
    # no. merge step is needed here.
    pivot = partition(start_idx, end_idx) # use two pointers for partition.
    quickSort(arr[start_idx : pivot])
    quickSort(arr[pivot: end_idx])
```
just three lines. beauty of recursive algo.

6. Quick Select - select the kth smallest element in the array.

Approach - We use the quick sort algo. We get our pivot index p.

if k < p = we search on left half.
if k > p = we search on right half.
if k == p = we return it as the answer.

7. Count Sort = Dutch National Flag.

Time Comlexity = O(n) + O(range).

_Time complexity of printing is O(n) because the total process would be executed at most n times._

8. Radix Sort = Use of stability. sort from the last index to first index and keep ordering. (use count sort in each iteration.)

9. Given an array generate all possible subsets, return the sum of {max(subset) - min(subset)} for every subset.

Observation - Think in terms of contribution. Similiar approach as submatrix sum and hamming distance.
Positive contribution - no. of subsets in which it is the maximun. 2^i
Negative contribution - no. of subsets in which it is the minimum. 2^(len-i-1)

10. Game of bottles.

Example where sorting is not necessary.
Observation - The max number of stacks created is the max repitition of any element.