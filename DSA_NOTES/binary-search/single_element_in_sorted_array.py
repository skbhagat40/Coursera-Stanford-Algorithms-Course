"""
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
"""

#Observation - sorted array - pairs occur together.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        lo = 0
        hi = len(A) - 1
        while lo<=hi:
            mid = (lo + hi)//2
            if mid == 0:
                if A[mid] != A[mid + 1]:
                    return A[mid]
                lo = mid + 1
                continue
            if mid == len(A)-1:
                if A[mid] != A[mid - 1]:
                    return A[mid]
                hi = mid - 1
                continue
            if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
                return A[mid]
            else:
                if A[mid] == A[mid+1]:
                    if mid % 2 == 0:
                        lo = mid + 2
                    else:
                        hi = mid - 1
                elif A[mid] == A[mid - 1]:
                    if (mid - 1) % 2 == 0:
                        lo = mid + 1
                    else:
                        hi = mid - 2