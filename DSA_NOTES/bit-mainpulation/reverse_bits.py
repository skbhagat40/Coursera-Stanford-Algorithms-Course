"""
Reverse the bits of an 32 bit unsigned integer A.
"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans = 0
        for i in range(31,-1,-1):
            #use formula bit a position i is replaced by bit at position 31 - i.
            bit = (A & (1<<(31-i)))
            if bit >= 1:
                # print(bit, i)
                ans |= (1<<i)
        return ans
"""
Intution - use the formula. bit a position i is replaced by bit at position 31 - i.
same as matrix rotation question.
check if bit is 1, then replace it.
"""