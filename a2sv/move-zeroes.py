class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        indx , nonZero = 0,0
        while nonZero < len(nums):
            if nums[nonZero] != 0:
                nums[indx] ,nums[nonZero] = nums[nonZero], nums[indx]
                indx +=1
            nonZero +=1
        return nums
                
            
        

        
        