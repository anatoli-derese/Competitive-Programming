class Solution:
    def  twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            holder=nums.copy()
            otherNumber = target - nums[i]
            holder.pop(i)
            if otherNumber in holder:	
                return (i,holder.index(otherNumber)+1)
        
        
             
									
					

								
	            
     
     