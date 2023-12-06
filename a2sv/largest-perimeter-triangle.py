class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def canForm(a,b,c):
            if a + b > c and a + c > b and c + b > a:
                return True
            return False
        l, r = 0,2
        nums.sort(reverse = True)
        while r < len(nums):
            if canForm(nums[l], nums[l+1], nums[r]):
                return sum(nums[l:r+1])
            r +=1
            l +=1
        return 0