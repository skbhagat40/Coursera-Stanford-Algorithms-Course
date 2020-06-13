"""
Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. We ensure that answer will be unique. 
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        lo = 0
        hi = len(A) - 1
        # always look on the greater side.
        while lo <= hi:
            mid = (lo + hi)//2
            if mid == 0:
                if A[mid] >= A[mid+1]: # without equality was giving overflow
                    return A[mid]
                lo = mid + 1
                continue
            if mid == len(A)-1:
                if A[mid] >= A[mid - 1]:
                    return A[mid]
                hi = mid - 1
                continue
            if A[mid] >= A[mid + 1] and A[mid] >= A[mid - 1]: # should come before the other two.
                return A[mid]
            elif A[mid] < A[mid+1]:
                lo = mid + 1
            elif A[mid] > A[mid+1]:
                hi = mid - 1