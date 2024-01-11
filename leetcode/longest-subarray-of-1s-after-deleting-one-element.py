class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0
        zeroI = []
        ans = -float('inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                zeroI.append(i)
            if zeros > 1:
                left = zeroI[-2] + 1
                zeros -=1
            ans = max(ans, i- left )
        return ans