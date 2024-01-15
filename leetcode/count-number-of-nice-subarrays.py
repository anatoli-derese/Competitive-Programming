class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count , ans, left, subArr = 0,0,0,0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count +=1
                subArr = 0
            while odd_count == k and left < len(nums):
                if nums[left] % 2 == 1:
                    odd_count -=1
                left +=1
                subArr +=1
            ans += subArr
        return ans