"""
Divide two integers without using multiplication, division and mod operator. Return the floor of the result of the division. Example:
"""
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def divide(self, A, B):
	    r,count = 0,0
	    ans = 0
	    a = abs(A)
	    b = abs(B)
	    temp = 0
	    for i in range(31,-1,-1):
	        if (b<<i) > a:
	            continue
	        else:
	            a -= b<<i
	            ans |= (1<<i)
	            if ans == a:
	                break
	    flag = None
	    if ans >= 2**31 - 1:
	        flag = True
	        ans = 2**31 - 1
	    if (A>0 and B>0) or (A<0 and B<0):
	        ans =  ans
	    else:
	        ans =  -1 * ans
	        if flag:
	            ans -= 1
	    return ans

"""
Intution - A = B*answer + c.
B*x < A.
We need to maximize the value of x.

Key observation = a<<i is equivalent to multiplying a by 2, i times.
To find msb of x, we can start i from 32 and check B<<i < A.
Now, we need to form the other bits - 
A -= B<<i, and we repeat the same process.
"""