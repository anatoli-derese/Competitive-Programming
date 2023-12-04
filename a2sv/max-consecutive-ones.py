class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r = 0, 0
        ans = 0
        d = {0:0, 1:0}
        while r < len(nums):
            d[nums[r]] +=1
            if d[0] == 0:
                ans = max(ans, r - l +1)
            while d[0] > 0:
                d[nums[l]] -=1
                l +=1
            r +=1
        return ans


        