# problem statement - https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
Solution-
class Solution:
    def dfs_helper(self,node,path,target,res):
        if node is not None:
            #print("visiting",node)
            path = path + [node]
            if node == target:
                res.append(path)
                return path
            else:
                for el in self.graph[node]:
                    if el not in path:
                        disc = self.dfs_helper(el,path,target,res)
                        
            return res
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # let's implement the dfs here
        self.visited = [False]*len(graph)
        self.graph = graph
        res = self.dfs_helper(0,[],len(graph)-1,[])
        return res
