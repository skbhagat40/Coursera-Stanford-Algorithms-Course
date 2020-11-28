"""
https://github.com/skbhagat40/LeetCode-Challanges/blob/master/november/26.py
"""
from collections import Counter, defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for u_w_c in range(1, 27):
            i, j = 0, 0
            moreEqK = 0
            arr = [0]*27
            Found = 0
            while j < len(s) and i < len(s) and i <= j:
                if j >= len(s):
                    break
                if moreEqK <= u_w_c:
                    # handle case 1. shift towards right.
                    if arr[ord(s[j]) - ord('a')] == 0:
                        moreEqK += 1
                    arr[ord(s[j]) - ord('a')] += 1
                    if arr[ord(s[j]) - ord('a')] == k:
                        Found += 1
                    j += 1
                else:
                    # handle case 2. shift towards left. shift the window
                    if arr[ord(s[i]) - ord('a')]  == k:
                        Found -= 1
                    arr[ord(s[i]) - ord('a')] -= 1
                    if arr[ord(s[i]) - ord('a')] == 0:
                        moreEqK -= 1
                    i += 1
                if Found == len(list(filter(lambda x: x>0, arr))):
                    ans = max(ans, j-i)
                
        return ans
                    
