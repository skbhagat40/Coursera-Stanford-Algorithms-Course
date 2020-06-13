"""
Given an integer A.
Two numbers X and Y are defined as follows:
X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
return X ^ Y
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        B = A
        count = 0
        r = 0
        while B>0:
            count += 1
            if B & 1:
                pass
            else:
               r = r | (1<<count-1)
            B = B>>1
        return (r)^(1<<count)

"""
Intution - Addition in Binary is like xor operation (if we ignore the carry). 
To find the greatest number less than A for which sum and xor sum are equal - 
** Take 2's complement. In that case sum and xor sum will be same. And the resulting number will be smaller than A.
101 => 010
To find the greatest number greater than A for which sum and xor sum are same - 
1<<(no. of digits in A). => place one in next higher bit position of A and rest bits will be 0.
101 => 1000
"""

# My Implementation of 2's compliment - 
def two_s_compliment(B):
    r,count = 0,0
    while B>0:
        count += 1
        if B & 1:
            pass
        else:
            r = r | (1<<count-1)
        B = B>>1
"""
Intution - Track zeros and set those bits to one using OR operation.
Leave 1's . They automatically become 0.
"""