class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = float('inf')
        maximum = float('-inf')
        max_dict ={}
        min_dict ={}
        # setting the maximum values
        for i in range(len(nums)-2, -1, -1):
            max_dict[i] = max(maximum, nums[i+1])
            maximum = max_dict[i]
        # setting the minimum values
        
        for i in range(1,len(nums)):
            min_dict[i] = min(minimum, nums[i-1])
            minimum = min_dict[i]
        # checking the cases
        for i in range(1,len(nums)-1):
            if nums[i] > min_dict[i] and nums[i] < max_dict[i]:
                return True
        return False
            

