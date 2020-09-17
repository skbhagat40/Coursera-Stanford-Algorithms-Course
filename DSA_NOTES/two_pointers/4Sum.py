from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # let's try hashset based approach.
        p_s  = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p_s[nums[i] + nums[j]].append([i, j])
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                to_f = target - nums[i] - nums[j]
                if to_f in p_s:
                    for p in p_s[to_f]:
                    # p = p_s[to_f]
                        if i != p[0] and i != p[1] and j != p[0] and j != p[1]:
                            res.append(sorted([nums[i], nums[j], nums[p[0]], nums[p[1]]]))
        ans =  sorted(res)
        res = []
        for el in ans:
            if len(res) == 0 or el != res[-1]:
                res.append(el)
        return res
