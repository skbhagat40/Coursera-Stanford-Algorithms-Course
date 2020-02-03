class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = 0
        local_max = 0
        for el in nums:
            if el > 0:
                local_max += el
            if el < 0:
                if el + local_max > 0:
                    local_max += el
                else:
                    local_max = 0
            if local_max > global_max:
                global_max = local_max
        if global_max == 0:
            return max(nums)
        return global_max
        
