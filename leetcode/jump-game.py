class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good = len(nums)-1
        flag = True
        j = len(nums) -1
        while j >= 0:
            if nums[j] + j >= last_good:
                flag = True
                last_good = j
            else:
                flag = False
            j -=1
        return flag
        