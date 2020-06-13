"""
Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.
"""

# think in terms of initialization, base condition and recursive steps.

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def permute(self, A):
        self.ans = []
        self.per(0, A)
        return self.ans
    def per(self, current_index, arr):
        """
            Since, the array for each recursive step is diff, we need to pass that also.
        Arguments:
            current_index {[type]} -- [description]
            arr {[type]} -- [description]
        """
        if current_index == len(arr) - 1:
            # termination condition, no further possiblities left. add the answer to the result.
            self.ans.append(arr[:])
            return # imp! to avoid stack overflow

        s = set() # for handling repitions
        for i in range(current_index, len(arr)):
            if arr[i] not in s:
                s.add(arr[i])
                arr[current_index], arr[i] = arr[i], arr[current_index]
                self.per(current_index + 1, arr)
                arr[i], arr[current_index] = arr[current_index], arr[i] # reset the array back.
