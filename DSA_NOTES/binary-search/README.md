Binary Search.

Used for searching in a sorted array.
nlogn runtime.
Can be used if following conditions are met -

1. Order in search space.
2. Able to make decision to discard portion of serach space.
3. function should be montonous.
4. There must be a fixed reference to search for.

Applications of Binary Search -

1. Count first occurance. Slight variation on Binary Search. If element is found, binary search on left.
2. Count last occurance.
3. Count total occurances.

Applications of binary search where array is not sorted -

Helpful Tip - Make Graph of the search space.

1. Binary search in sorted array which is rotated. All Elements are unique.

First we need to find the pivot. (i.e. the no. of rotations). Special property of the pivot - element on the left of pivot and right of pivot are greater than it.

Approach - We can use binary search to find the pivot element. We need a **reference point** based on which we can make a decision.(either to move left or right.) and a **decision criteria**.

Observation - pivot will always lie in the second part. And all values of second part are less than A[N-1]. All values of first part are > A[n-1].

decision criteria - If A[i] > A[N-1], discard left. If A[i] < A[N-1], discard right.(similiar to finding first occurance.)

2. Find single number in an array in logN. (All pairs occur together.)
   e.g. [9,9,2,2,3,3,5,7,7].

   Observation = before single element, in all pairs, the first occurance is even index, and second 
   occurance is odd index. We can use this observation to make decision.

   **reference point** - unique index. **decision_criteria** - index is odd/even.

3. Finding peak in an unsorted array.

Observation - always move to next greater element. discard the lower part.

**Another Important Concept is Binary Search on all possible answers.**

Applications - 

1. Median of a matrix. (sorted by row)
2. Special Integer. (Includes use of 2 pointers/ sliding window.)
3. Find Height of Staircase.

Other problems using binary search on answer space.

1. Aggresive Cows - Place the cows such that they are maximum distance Apart.

Observation - If D is a possible answer, then >D is also possible.
min_dist = 1
max_dist = D[-1] - D[0]

Binary search on the answer space.
_possible function_ - 

```
def possible(dist):
   last = D[0]
   count = 0
   for i in range(1,len(D)):
      if D[i] - last >= dist:
         count += 1
         last = D[i]
   return count >= B
```

2. Books Allocation - Allocate Books , in a way which minimizes the maximum number of pages allocated to a student. (No. of Books >= Number of students.). No book shall be left unallocated.

_Similiar to time required to paint a board i.e painter partition_

Observation - 

If it is possible to allocate  a maximum of B pages, then it will also be possible to allocate a maximum >B pages.

We have to minimize the no. of pages , so we will search in lesser answer space.

```
def possible(val):
   count = 0
   s = B[0]
   for i in range(1, len(val)):
      if s <= val:
         pass
      else:
         count += 1 # being greedy here, need to save minimize possiblites for future books.
         s = B[i]
   return count <= B
```

3. Painter Partition - Partition the board space among the painters in order to minimize
the time taken to complete the whole board. Can only allocate continuos board spaces to painters.

Observation - Similiar to Book Partition. Need to minimize the max. paint space allocated to a painter.

4. Smallest Good Base - 
   
   Approach = linear search over possible digits.
   Binary search for (checking possible) with fixed no. of digits.

   The problem here is both base and no. of digits are varying, so can't apply binary search here.
   If we fix the no. of digits then we can use binary search for base.
   Return the minimum base among all possibe bases for all values of digits.