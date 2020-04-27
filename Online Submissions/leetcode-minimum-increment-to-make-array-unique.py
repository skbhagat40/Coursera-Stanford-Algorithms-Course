# https://leetcode.com/problems/minimum-increment-to-make-array-unique/submissions/
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = 0
        if len(A) == 0:
            return 0
        counts_arr = [0] * (10*max(max(A),1) + 1)
        for el in A:
            counts_arr[el] += 1
        while not all(map(lambda x: x==1 or x==0, counts_arr)):
            for idx,el in enumerate(counts_arr):
                if el > 1:
                    # print(el, counts_arr)
                    counts_arr[idx] = 1
                    counts_arr[idx+1] += el-1
                    count += el-1
        return count
"""
Things learned can't iterate over a dictionary while changing it's values.
using array to mantain frequencies and iterate over the array not the copy.
in case of deletion iterate over copy and do some len checking.
"""
