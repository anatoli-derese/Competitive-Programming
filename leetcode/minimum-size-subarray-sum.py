class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        prefix_sum = [0]* (len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        ans = float('inf')
        while r <= len(nums):
            temp = prefix_sum[r]- prefix_sum[l]
            if temp >= target:
                ans = min(ans, r - l)
                l += 1
            elif temp < target:
                r +=1
        if ans == float('inf'):
            return 0
        return ans
        