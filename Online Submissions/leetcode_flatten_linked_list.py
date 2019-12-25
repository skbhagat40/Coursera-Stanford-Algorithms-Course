# problem link - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.arr = []
        if head is None:
            return None
        self.traverse(head)
        for idx,val in enumerate(self.arr):
            if idx == 0:
                val.next = self.arr[idx + 1]
                val.child = None
            if idx == len(self.arr) - 1:
                val.prev = self.arr[idx -1]
                val.child = None
            else:
                val.next = self.arr[idx + 1]
                val.prev = self.arr[idx -1]
                val.child = None
        self.arr[0].prev = None
        return self.arr[0]
    def traverse(self,head):
        if head is not None:
            self.arr.append(head)
        if head is not None and head.child is not None:
            self.traverse(head.child)
        if head is not None and head.next is not None:
            self.traverse(head.next)
