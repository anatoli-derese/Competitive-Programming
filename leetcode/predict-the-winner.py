class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(i,j, one):
            if i == j:
                return nums[i] 
            if i > j:
                return 0
            if one:
                one = False
                start = rec(i+1 , j , one) + nums[i]
                end = rec(i,j -1, one) + nums[j]
                return max(start,end)
            else:
                one = True
                start = rec(i+1, j, one) - nums[i]
                end = rec(i,j-1,one) - nums[j]
                return min(start,end)                

        return rec(0, len(nums)-1, True) >=0
        