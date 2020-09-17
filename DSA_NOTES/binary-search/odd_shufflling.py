"""
sorted array, partition the odd indices, into left and right, swap them. Even indices stay as they are.
"""
"""
Intution = first try to find B in sorted even array. If it is equal, we got our answer.
If we get some other number, then it means it was swapped with B. Now, we need to find the swapped number.
Use binary search over even indices to do that.
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lo = 0
        hi = (len(A)-1)//2
        ans = float('-inf')
        ans_idx = None
        # first search over all even indices
        while lo <= hi:
            mid = (lo + hi)//2
            if A[mid * 2] == B:
                return mid * 2
            else:
                if A[mid * 2] > B:
                    hi = mid - 1
                else:
                    ans = max(ans, A[mid * 2])
                    ans_idx = mid * 2
                    lo = mid + 1
        if A[ans_idx + 1] == B:
            return ans_idx + 1
        to_find = A[ans_idx + 1] # this is the number that was swapped
        # in binary search try to find, this smaller or larger number.
        lo = 0
        hi = (len(A)-1)//2
        ans = float('-inf')
        ans_idx = None
        # first search over all even indices
        while lo <= hi:
            mid = (lo + hi)//2
            if A[mid * 2] == to_find:
                return mid * 2
            else:
                if A[mid * 2] > to_find:
                    hi = mid - 1
                else:
                    ans = max(ans, A[mid * 2])
                    ans_idx = mid * 2
                    lo = mid + 1
        # print('ans', ans_idx, to_find, ans)
        if A[ans_idx + 1] == B:
            return ans_idx + 1
        if A[ans_idx - 1] == B:
            return ans_idx - 1
        if A[ans_idx + 3] == B:
            return ans_idx + 3
        if A[ans_idx - 3] == B:
            return ans_idx - 3
        return - 1
        
