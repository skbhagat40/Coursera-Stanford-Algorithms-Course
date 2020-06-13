"""
You have an array A[] with N elements. We have 2 types of operation available on this array :
We can split a element B into 2 elements C and D such that B = C + D.
We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P and Q.
You have to determine whether it is possible to make array A[] containing only 1 element 0 after several splits and/or merge?
"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        from functools import reduce
        r = reduce(lambda x,y: x^y, A)
        return "Yes" if r%2 == 0 else "No"

"""
Intution - merge all elements to single, return it can be split into two equal values or not.
Need more clarification on this though.
"""