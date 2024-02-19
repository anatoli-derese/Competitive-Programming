class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(2*len(nums)):
            i = i % len(nums)
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                val = stack.pop()
                ans[val] = nums[i]
            stack.append(i)
        return ans

            
        