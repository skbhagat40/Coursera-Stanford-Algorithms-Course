You are given an array A consisting of heights of Christmas trees, and an array B of same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 such trees, so they have the minimum cost and find the minimum cost.

If not possible to choose 3 such trees, return -1.

Solution
```
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        min_vals = [None] * len(A)
        ans = float('inf')
        for i in range(1, len(A)):
            m = float('inf')
            for j in range(i):
                if A[j] < A[i]:
                    if B[j] < m:
                        m = B[j]
                        min_vals[i] = j
                    if min_vals[j] is not None:
                        ans = min(ans, B[min_vals[j]] + B[i] + B[j] )
        return ans if ans != float('inf') else -1
```

Approach - for each index store the min. B[i] before it which staisfies the condition A[j] < A[i]. for each i iterate, we already have one fixed no i with cost B[i]
. The other is j and the third is the min. which we found for j in previous iterations. This is memoization, one of the most useful techniques in arrays.
