class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max  = acc = nums[0]
        for i in range(1, len(nums)):
            acc = max(acc + nums[i], nums[i])
            _max = max(_max, acc)
        return _max

        