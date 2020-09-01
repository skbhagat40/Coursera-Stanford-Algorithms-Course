from collections import defaultdict
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        g = defaultdict(list)
        for word in A:
            g[word[0]].append(word)
        chars = [0]*26
        # out_order = [-1]*26
        starts = (word[0] for word in A)
        f = False
        fw = []
        for word in A:
            chars[ord(word[0]) - ord('a')] += 1
            if word[0] == word[-1]:
                if word[0] in [x[-1] for x in A if x != word]:
                    f = True
                fw.append(word)
            chars[ord(word[-1]) - ord('a')] -= 1
        if all(map(lambda x: x == 0, chars)) and f:
            res =  True
        else:
            return 0
        # check for strongly connected
        vis = defaultdict(int)
        def dfs(root):
            # path = path + [root]
            vis[root] = 1
            # if len(path) == len(set(A)):
                # if path[0][0] == path[-1][-1]:
                    # return 1
            for child in g.get(root[-1], []):
                if not vis[child]:
                    dfs(child)
                    # if res:
                        # return 1
        def dfs_r(root):
            # path = path + [root]
            vis[root] = 1
            # if len(path) == len(set(A)):
                # if path[0][0] == path[-1][-1]:
                    # return 1
            for child in g.get(root[0], []):
                if not vis[child]:
                    dfs(child)
                    # if res:
                        # return 1
                        
        res = dfs(A[0])
        f1 = len(list(filter(lambda x: x == 1, vis.values())))
        vis = defaultdict(int)
        for word in A:
            g[word[-1]].append(word)
        res = dfs_r(A[0])
        f2 = len(list(filter(lambda x: x == 1, vis.values())))
        res = f1 and f2
        return 1 if res else 0
        return 0
        i