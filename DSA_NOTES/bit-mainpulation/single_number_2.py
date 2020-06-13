"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.
* was not able to come up with optimal solution.
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	   ans = 0
	   for i in range(32):
	       s = 0
	       for el in A:
	           if (el & (1<<i)):
	               s += 1
	       if s%3 == 1:
	           ans |= (1<<i)
	   return ans
"""
Intution - sum the ith bit of all elements in the array. the ith bit of answer will be set if,
sum % 3 == 1.
Each bit can occur at max multiple of 3(since, others repeat 3 times.) + 1 times(if it is present in the answer also).
"""