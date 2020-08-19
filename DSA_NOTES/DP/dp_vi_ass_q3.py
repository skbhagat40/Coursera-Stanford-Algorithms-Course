"""
Maximum Difference on Tree
"""
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        tree = defaultdict(list)
        root = 1
        for s, d in B:
            tree[s].append(d)
            tree[d].append(s)
        ans = 0
        def post_order(parent, root):
            if root is None:
                return (0, 0)
            children = tree.get(root, [])
            min_l = max_l = md_l = min_r = max_r = md_r = 0
            min_val = max_val = A[root-1]
            for l in children:
                nonlocal ans
                if  l != parent:
                    min_l, max_l = post_order(root, l) or (0, 0)
                    min_val =  min(min_l, min_val)
                    max_val = max(max_val, max_l)
                    ans = max(ans, A[root-1] - min_l, max_l - A[root -1])
            return min_val, max_val
        res = post_order(0, 1)
        return ans
        
     """
     Conceptual mistakes that I was doing - 1. Not adding reverse edges. 2. considering a node has only 2 branches. 3. Not checking for loops.
     One good way here is passing the parent, and checking 
     """
