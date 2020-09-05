class DSU:
    def __init__(self, A):
        self.categories = [x for x in range(A+1)]
        self.sizes = [1 for x in range(A+1)]
        # considering each node as it's own category
        
    def find(self, node):
        # recursive code.
        if self.categories[node] == node:
            return node
        else:
            return self.find(self.categories[node])
        # TODO need to add the path compression optimization
        
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        # do the union only when the parents are not equal.
        if parent1 != parent2:
            size1 = self.sizes[parent1]
            size2 = self.sizes[parent2]
            if size1 <= size2:
                self.categories[parent1] = parent2
                self.sizes[parent2] += size1
            else:
                self.categories[parent2] = parent1
                self.sizes[parent1] += size2
        # Done !!
    
class Solution:
	# @param A : integer
	# @param B : list of list of integers
	# @return an integer
	def solve(self, A, B):
	    dsu = DSU(A)
	    ans = 0
	    # sort the edges
	    sorted_edges = sorted(B, key=lambda x : x[2]) # edges sorted by weight
	    for edge in sorted_edges:
	        a, b, w = edge
	        if dsu.find(a) != dsu.find(b):
	            ans += w
	            dsu.union(a, b)
	    return ans
