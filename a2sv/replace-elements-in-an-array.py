class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {nums[i]: i for i in range(len(nums))}
        for x,r in operations:
            indx = d[x] 
            nums[indx] = r 
            del d[x]   
            d[r] = indx 
            
        return nums