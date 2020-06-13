"""
Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 ... A .
"""
"""
Intution - We try to build a recursion tree, based on the following fact - 

    a. At first position we can have N elemnts. (No. of nodes at the top level of the recursion tree.) 
    b. for successive recursions we exclude the first element from the array.

"""

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
    def combine(self, A, B):
        self.B = B
        self.ans = []
        self.arr = range(1, A+1)
        self.combos(0,range(1, A+1),[])
        return self.ans
    def combos(self, current_index, arr, subset):
        # arr is used to store the choices left.
        if current_index == self.B:
            self.ans.append(subset[:])
            return
        # else create the recursion tree.
        for i in range(len(arr)):
            # keep in mind eliminating the further choices.
            self.combos(current_index + 1, arr[i+1:], subset + [self.arr[i]]) # add the current element to the subset, to keep building combinations based on it.