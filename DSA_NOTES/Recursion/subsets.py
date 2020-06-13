"""
Given a set of distinct integers, A, return all possible subsets
"""

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def subsets(self, A):
        self.ans = []
        self.arr = A
        # since the array is constant here, only current index is varying, we don't need to pass the array 
        # everywhere
        self.gen_subs(0,[])
        return self.ans
    def gen_subs(self, current_index, subset):
        # termination condition
        if current_index == len(self.arr):
            # we looked at all possiblites, still need to add current subset to the answer.
            self.ans.append(subset[:])
            return
        self.gen_subs(current_index+1,subset) # don't include current element in the subset.
        self.gen_subs(current_index+1, subset + [self.arr[current_index]]) # include it and build the recursion tree.