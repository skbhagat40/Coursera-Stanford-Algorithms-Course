class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        counters = [Counter(w) for w in A]
        to_ret = []
        min_word = min(counters, key = lambda x: len(x))
        for char in min_word:
            if all(list(map(lambda x: char in x, counters))):
                to_ret.append((char, min([q[char] for q in counters])))
        res = []
        for el in to_ret:
            for t in range(el[1]):
                res.append(el[0])
        return res
