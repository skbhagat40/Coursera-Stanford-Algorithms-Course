# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        res = []
        initpath = [root]
        list_of_paths = [initpath]
        while list_of_paths:
            children = []
            subpath = list_of_paths.pop(0)
            to_explore = subpath[-1]
            if to_explore.left == None and to_explore.right == None :
                temp = [el.val for el in subpath]
                s = 0
                for el in temp:
                    s += el
                if s==sum:
                    res.append(temp)
            else:
                if to_explore.left is not None:
                    children.append(to_explore.left)
                if to_explore.right is not None:
                    children.append(to_explore.right)
                for child in children:
                    if child not in subpath:
                        list_of_paths.append(subpath+[child])
        return res