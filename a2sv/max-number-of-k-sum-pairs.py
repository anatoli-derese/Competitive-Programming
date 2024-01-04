class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0 , len(nums)-1
        ans = 0
        while i < j:
            if nums[i] + nums[j]== k :
                i +=1
                j -=1
                ans +=1 
            elif nums[i] + nums[j] < k:
                i +=1
            else:
                j -=1
        return  ans
        