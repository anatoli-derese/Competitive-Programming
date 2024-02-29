class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            dashes = math.ceil(nums[i] / last)
            ans += dashes -1
            last = nums[i] // dashes
        return ans
        