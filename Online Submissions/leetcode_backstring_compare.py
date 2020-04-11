# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/#.XpGqgruWieM.linkedin

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while S[0] == '#':
            S = S[1:]
        while T[0] == '#':
            T = T[1:]
        # let's take a recursive apporoach similiar to that of palendromic string comparision.
        return self.compare(S, T, 0, 0)
    def compare(self, S, T, s_hash_count, t_hash_count):
        if len(S) == 0 and t_hash_count > 1:
            return True
        if len(T) == 0 and s_hash_count > 1:
            return True
        if s_hash_count < 0:
            s_hash_count = 0
        if t_hash_count < 0:
            t_hash_count = 0
        if len(S) == 0 and len(T) == 0:
            return True
        if len(S) == 1 and len(T) == 1:
            if S == '*' and t_hash_count > 0:
                return True
            if T == '*' and s_hash_count > 0:
                return True
            if (s_hash_count != t_hash_count):
                return False
            if (s_hash_count == t_hash_count and (s_hash_count > 0 and t_hash_count >0)):
                return True
            else:
                return (S[0] == T[0])
        if len(S) == 0:
            S = '*'
        if len(T) == 0:
            T = '*'
        char_s = S[-1]
        char_t = T[-1]
        if char_s == '#':
            s_hash_count += 1
        else:
            s_hash_count -= 1
        if char_t == '#':
            t_hash_count += 1
        else:
            t_hash_count -= 1
        if s_hash_count >= 0 and t_hash_count >= 0:
            # print('I am returning', S, T, s_hash_count, t_hash_count)
            return True and self.compare(S[:-1], T[:-1], s_hash_count, t_hash_count)
        if s_hash_count >= 0 and t_hash_count < 0:
            return True and self.compare(S[:-1], T, s_hash_count, t_hash_count)
        if t_hash_count >= 0 and s_hash_count < 0:
            return True and self.compare(S, T[:-1], s_hash_count, t_hash_count)
        if s_hash_count < 0 and t_hash_count < 0:
            return S[-1] == T[-1] and self.compare(S[:-1], T[:-1], s_hash_count, t_hash_count)
        
