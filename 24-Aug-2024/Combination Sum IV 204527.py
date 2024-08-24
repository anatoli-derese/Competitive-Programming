# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(tot):
            if tot == target:
                return 1
            # if i >= len(nums):
            #     return 0
            if tot > target:
                return 0
            ans = 0
            for i in range(len(nums)):
                ans += dp(tot+nums[i]) 
            return ans
        
        return dp(0)