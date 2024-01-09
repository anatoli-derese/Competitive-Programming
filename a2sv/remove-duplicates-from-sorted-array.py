class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j ,k= 0,1,0
        while i < len(nums)- 2:
            temp = nums[i]
            while j < len(nums) - 1 and nums[j] == temp :
                j += 1 
            i +=1
            k +=1
            nums[i] = nums[j]          
        i,j =0,1
        res = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return res
            i +=1
            j +=1
            res +=1
        return res

            
