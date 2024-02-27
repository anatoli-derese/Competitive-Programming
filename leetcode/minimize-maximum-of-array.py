class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        wind = res = nums[0]
        
        for i in range(1, len(nums)):
            wind += nums[i]
            avg = math.ceil(wind / (i+1))
            res = max(res, avg)
        return res
        