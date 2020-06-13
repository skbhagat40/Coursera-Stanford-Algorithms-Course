"""
Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        from functools import reduce
        res = reduce(lambda x,y: x^y, A)
        p = 0
        while not (res & (1<<p)):
            p += 1
        xor1, xor2 = 0,0
        for el in A:
            if el & (1<<p):
                xor1 ^= el
            else:
                xor2 ^= el
        return sorted([xor1, xor2])
"""
Intution - get first set bit of resulting xor(p), make two sets, return their xor.
Key Idea - XOR of a and b gives the bits where a and b differ.(helps in identifying unique occurance. a^a=0, a^0=a)
"""