# url - https://leetcode.com/problems/custom-sort-string/
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        temp, pos = [], []
        neg = []
        visited = [False] * len(T)
        for el in range(len(S)):
            for k in range(len(T)):
                if S[el] == T[k]:
                    visited[k] = True
                    temp.append(S[el])
                    pos.append(el)
        res = "".join(temp)
        for el in range(len(T)):
            if not visited[el] and T[el] in res:
                a = res.index(T[el])
                res = res[:a] + T[el] + res[a:]
            elif not visited[el]:
                res += T[el]

        return res
