"""
String split, such that in each part only one char occurs.
use single, traversal, if cross the rightmost occurance, update it
"""
# Implementation

def partition_string(S):
  right_most = {c: i for i, c in enumerate(S)}
  left_pos = 0
  ans = []
  for i in range(len(S)):
    char = S[i]
    if right_most[char] == i:
      ans.append(i-left_pos)
      left_pos = i + 1
  return ans
