class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = 0
        ans = -float('inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros +=1
            while zeros > k and left < len(nums):
                if nums[left] == 0:
                    zeros -=1
                left += 1
            ans = max(ans, i-left + 1)
        return ans


        